require 'rails_helper'
require 'vcr'

VCR.configure do |configure|
  configure.cassette_library_dir = "spec/vcr_cassettes"
  configure.hook_into :webmock
  configure.register_request_matcher :uri_regex do |request1, request2|
    request1.uri.match(request2.uri)
  end
  configure.filter_sensitive_data('<TELNYX_API_KEY>') { ENV['TELNYX_API_KEY'] }
end

# Stub Telnyx API calls in tests
RSpec.configure do |c|
  c.before(:each) do
    # Stub Telnyx Configuration to avoid real API calls
    allow(Telnyx).to receive(:api_key=)
    
    # Stub AvailablePhoneNumber.list to return mock data
    mock_phone = OpenStruct.new(phone_number: '+16195559999')
    mock_list = OpenStruct.new(data: [mock_phone], first: mock_phone)
    allow(Telnyx::AvailablePhoneNumber).to receive(:list).and_return(mock_list)
    
    # Stub NumberOrder.create
    mock_order = OpenStruct.new(
      id: 'order_123',
      status: 'pending',
      phone_numbers: [OpenStruct.new(phone_number: '+16195559999')]
    )
    allow(Telnyx::NumberOrder).to receive(:create).and_return(mock_order)
    
    # Stub Message.create
    mock_message = OpenStruct.new(
      id: 'msg_123',
      status: 'queued',
      state: 'queued'
    )
    allow(Telnyx::Message).to receive(:create).and_return(mock_message)
  end
end

module Params
  # Add more helper methods to be used by all tests here...

  def user_params(params={})
    {
      password: "hello55",
      email: "jard@example.com",
      name: "Jard",
      phone_number: "6195559090",
      country_code: "+1"
    }.merge(params)
  end

  def reservation_params()
    {
      name: "reservation1",
      guest_phone: "6195559090",
      message: "message1",
      property_id: 1,
    }
  end
end

RSpec.configure do |c|
  c.include Params
end
