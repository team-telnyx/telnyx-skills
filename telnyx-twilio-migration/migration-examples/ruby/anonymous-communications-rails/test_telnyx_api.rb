#!/usr/bin/env ruby

require 'bundler/setup'
require 'telnyx'
require 'dotenv'
require 'logger'

Dotenv.load

puts "Testing Telnyx API connectivity..."
puts "TELNYX_API_KEY: #{ENV['TELNYX_API_KEY']&.slice(0, 10)}..."
puts "TELNYX_PHONE_NUMBER: #{ENV['TELNYX_PHONE_NUMBER']}"

begin
  # Setup Telnyx client
  Telnyx.api_key = ENV['TELNYX_API_KEY']

  puts "\n1. Testing Number Lookup..."
  # Test 1: List available phone numbers (validate API key)
  available_numbers = Telnyx::AvailablePhoneNumber.list(
    filter: {
      country_code: 'US',
      phone_number_type: 'local'
    },
    page: { size: 1 }
  )
  puts "   SUCCESS: Found #{available_numbers.data.length} available number(s)"
  puts "   First number: #{available_numbers.data.first&.phone_number}"

  puts "\n2. Testing SMS Sending (REAL API CALL)..."
  puts "   Using messaging_profile_id: #{ENV['TELNYX_MESSAGING_PROFILE_ID']}"
  message = Telnyx::Message.create(
    from: ENV['TELNYX_PHONE_NUMBER'],
    to: '+15551234567',  # Test number
    text: "Test message from anonymous-communications-rails migration"
  )
  puts "   SUCCESS: Message sent!"
  puts "   Message ID: #{message.id}"
  puts "   State: #{message.state}"

rescue Telnyx::APIError => e
  puts "   ERROR (API): #{e.message}"
  puts "   Details: #{e.inspect}"
  puts "   HTTP Status: #{e.http_status}"
  puts "   JSON Body: #{e.json_body}"
rescue => e
  puts "   ERROR: #{e.class} - #{e.message}"
  puts e.backtrace.first(5).join("\n")
end

puts "\n--- API Test Complete ---"
