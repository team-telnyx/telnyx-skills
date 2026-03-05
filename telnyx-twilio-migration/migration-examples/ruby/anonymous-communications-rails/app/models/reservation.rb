class Reservation < ActiveRecord::Base
  validates :name, presence: true
  validates :guest_phone, presence: true

  enum status: [ :pending, :confirmed, :rejected ]

  belongs_to :vacation_property
  belongs_to :user, optional: true

  def notify_host(force = false)
    # Don't send the message if we have more than one and we aren't being forced
    if self.host.pending_reservations.length > 1 and !force
      return
    else
      message = "You have a new reservation request from #{self.name} for #{self.vacation_property.description}:

      '#{self.message}'

      Reply [accept] or [reject]."

      self.host.send_message_via_sms(message)
    end
  end

  def host
    @host = User.find(self.vacation_property[:user_id])
  end

  def guest
    @guest = User.find_by(phone_number: self.guest_phone)
  end

  def confirm!
    provision_phone_number
    self.update!(status: 1)
  end

  def reject!
    self.update!(status: 0)
  end

  def notify_guest
    if self.status_changed? && (self.status == :confirmed || self.status == :rejected)
      message = "Your recent request to stay at #{self.vacation_property.description} was #{self.status}."
      self.guest.send_message_via_sms(message)
    end
  end

  def send_message_to_guest(message)
    message = "From #{self.host.name}: #{message}"
    self.guest.send_message_via_sms(message, self.phone_number)
  end

  def send_message_to_host(message)
    message = "From guest #{self.guest.name}: #{message}"
    self.host.send_message_via_sms(message, self.phone_number)
  end

  private

  def provision_phone_number
    Telnyx.api_key = ENV['TELNYX_API_KEY']
    begin
      # Search for available phone numbers in the US
      available_numbers = Telnyx::AvailablePhoneNumber.list(
        filter: {
          country_code: 'US',
          phone_number_type: 'local'
        }
      )

      # Get the first available number
      number_to_purchase = available_numbers.first&.phone_number

      if number_to_purchase.nil?
        # Fallback: get any US local number
        available_numbers = Telnyx::AvailablePhoneNumber.list(
          filter: { country_code: 'US', phone_number_type: 'local' }
        )
        number_to_purchase = available_numbers.first&.phone_number
      end

      # Purchase the number
      if number_to_purchase
        number_order = Telnyx::NumberOrder.create(
          phone_numbers: [{ phone_number: number_to_purchase }],
          connection_id: ENV['TELNYX_CONNECTION_ID'],
          messaging_profile_id: ENV['TELNYX_MESSAGING_PROFILE_ID']
        )

        # Set the reservation.phone_number
        self.update!(phone_number: number_to_purchase)
      end

    rescue Exception => e
      puts "ERROR: #{e.message}"
      Rails.logger.error("Failed to provision phone number: #{e.message}")
    end
  end
end
