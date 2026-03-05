require 'test_helper'

RSpec.describe ReservationsController, type: :controller do
  fixtures :all

  before(:each) do
    @host = users(:one)
    @guest = users(:two)
    @vacation_property = VacationProperty.find(reservation_params[:property_id])
    @reservation = reservations(:two)
    # Need to login user to view properties
    session[:user_id] = @host.id
  end

  after(:each) do
    @host.destroy
  end

  describe "GET index" do
    it "has reservations" do
      get :index
      expect(response).to be_successful
      expect(assigns(:reservations)).not_to be_nil
    end
  end

  describe "POST accept_or_reject" do
    it "accepts reservations" do
      VCR.use_cassette("accept_or_reject_reservation", match_requests_on: [:method, :uri_regex]) do
        post :accept_or_reject, params: { From: @host.phone_number, Body: "accept"}
  
        expect(response).to be_successful
        reservation = Reservation.find_by(id: @host.id)
        expect(reservation.phone_number).to_not be_nil
        expect(reservation.status).to eq("confirmed")
      end
    end
  end

  describe "POST create" do
    it "redirects to vacation property" do
      VCR.use_cassette("create_reservation", match_requests_on: [:method, :uri_regex]) do
        post :create, params: { reservation: reservation_params}
        expect(response).to have_http_status(:redirect)
        expect(response).to redirect_to(@vacation_property)
      end
    end
  end

  describe "POST connect_host_to_guest_sms" do
    it "returns a TwiML response" do
      post :connect_guest_to_host_sms, params: { From: @guest.phone_number, Body: "message", To: @reservation.phone_number}
  
      expect(response).to be_successful
      expect(response.body).to include("<Message to=\"+16195551234\">message</Message>")
    end
  end

  describe "POST connect_guest_to_host_sms" do
    it "returns a TwiML response" do
      post :connect_guest_to_host_sms, params: { From: @host.phone_number, Body: "message", To: @reservation.phone_number}
  
      expect(response).to be_successful
      expect(response.body).to include("<Message to=\"+16195559091\">message</Message>")
    end
  end

  describe "POST connect_host_to_guest_voice" do
    it "returns a TwiML response" do
      post :connect_guest_to_host_voice, params: { From: @guest.phone_number, Body: "message", To: @reservation.phone_number}
  
      expect(response).to be_successful
      expect(response.body).to include("<Play>http://howtodocs.s3.amazonaws.com/howdy-tng.mp3</Play>")
      expect(response.body).to include("<Dial>+16195551234</Dial>")
    end
  end

  describe "POST connect_guest_to_host_voice" do
    it "returns a TwiML response" do
      post :connect_guest_to_host_voice, params: { From: @host.phone_number, Body: "message", To: @reservation.phone_number}
  
      expect(response).to be_successful
      expect(response.body).to include("<Play>http://howtodocs.s3.amazonaws.com/howdy-tng.mp3</Play>")
      expect(response.body).to include("<Dial>+16195559091</Dial>")
    end
  end


end
