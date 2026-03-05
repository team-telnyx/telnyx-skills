class ReservationsController < ApplicationController
  skip_before_action  :verify_authenticity_token, only: [:accept_or_reject, :connect_guest_to_host_sms, :connect_guest_to_host_voice]
  before_action :set_telnyx_params, only: [:connect_guest_to_host_sms, :connect_guest_to_host_voice]
  before_action :authenticate_user, only: [:index]

  # GET /reservations
  def index
    @reservations = current_user.reservations.all
  end

  # GET /reservations/new
  def new
    @reservation = Reservation.new
  end

  def create
    @vacation_property = VacationProperty.find(params[:reservation][:property_id])
    @reservation = @vacation_property.reservations.create(reservation_params)

    if @reservation.save
      flash[:notice] = "Sending your reservation request now."
      @reservation.host.check_for_reservations_pending
    else
      flash[:error] = @reservation.errors.full_messages.to_sentence
    end
    redirect_to @vacation_property
  end

  # webhook for telnyx incoming message from host
  def accept_or_reject
    # Telnyx webhooks are JSON with nested data.payload structure
    payload = request.body.read
    data = JSON.parse(payload) rescue {}
    event_data = data['data'] || {}
    event_payload = event_data['payload'] || {}

    # Extract fields from Telnyx webhook format
    incoming = event_payload.dig('from', 'phone_number') || params[:From]
    sms_input = (event_payload['text'] || params[:Body] || '').downcase

    begin
      @host = User.find_by(phone_number: incoming)
      @reservation = @host.pending_reservation
      if sms_input == "accept" || sms_input == "yes"
        @reservation.confirm!
      else
        @reservation.reject!
      end

      @host.check_for_reservations_pending

      sms_reponse = "You have successfully #{@reservation.status} the reservation."
      respond(sms_reponse)
    rescue Exception => e
      puts "ERROR: #{e.message}"
      sms_reponse = "Sorry, it looks like you don't have any reservations to respond to."
      respond(sms_reponse)
    end
  end

  # webhook for telnyx to anonymously connect the two parties (SMS)
  def connect_guest_to_host_sms
    # Guest -> Host
    if @reservation.guest.phone_number == @incoming_phone
      @outgoing_number = @reservation.host.phone_number

    # Host -> Guest
    elsif @reservation.host.phone_number == @incoming_phone
      @outgoing_number = @reservation.guest.phone_number
    end

    # Return TeXML-compatible XML (TwiML format works with Telnyx TeXML)
    response_xml = <<~XML
      <?xml version="1.0" encoding="UTF-8"?>
      <Response>
        <Message to="#{@outgoing_number}">#{@message}</Message>
      </Response>
    XML

    render xml: response_xml
  end

  # webhook for telnyx -> TeXML for voice calls
  def connect_guest_to_host_voice
    # Guest -> Host
    if @reservation.guest.phone_number == @incoming_phone
      @outgoing_number = @reservation.host.phone_number

    # Host -> Guest
    elsif @reservation.host.phone_number == @incoming_phone
      @outgoing_number = @reservation.guest.phone_number
    end

    # Return TeXML-compatible XML for voice calls
    response_xml = <<~XML
      <?xml version="1.0" encoding="UTF-8"?>
      <Response>
        <Play>http://howtodocs.s3.amazonaws.com/howdy-tng.mp3</Play>
        <Dial>#{@outgoing_number}</Dial>
      </Response>
    XML

    render xml: response_xml
  end


  private
    # Send an SMS back to the Subscriber
    def respond(message)
      response_xml = <<~XML
        <?xml version="1.0" encoding="UTF-8"?>
        <Response>
          <Message>#{message}</Message>
        </Response>
      XML

      render xml: response_xml
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def reservation_params
      params.require(:reservation).permit(:name, :guest_phone, :message)
    end

    # Load up Telnyx parameters from webhook payload
    def set_telnyx_params
      # Read and parse the JSON body (Telnyx webhooks are JSON)
      payload = request.body.read

      # Store raw body for signature verification if needed
      @raw_body = payload

      # Parse the JSON payload
      data = JSON.parse(payload) rescue {}
      event_data = data['data'] || {}
      event_payload = event_data['payload'] || {}

      # Extract fields from Telnyx webhook format
      # Telnyx: from.phone_number, text, to is an array
      @incoming_phone = event_payload.dig('from', 'phone_number') || params[:From]
      @message = event_payload['text'] || params[:Body]

      # For voice webhooks, the 'to' field contains the dialed number
      anonymous_phone_number = if event_payload['to'].is_a?(Array)
                                 event_payload['to'].first&.dig('phone_number')
                               else
                                 params[:To]
                               end

      @reservation = Reservation.where(phone_number: anonymous_phone_number).first
    end
end
