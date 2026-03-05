ENV['RAILS_ENV'] ||= 'test'
require File.expand_path('../config/environment', __dir__)
require 'rails/test_help'
require 'mocha/minitest'

class ActiveSupport::TestCase
  # Setup all fixtures in test/fixtures/*.yml for all tests in alphabetical order.
  fixtures :all

  # Add more helper methods to be used by all tests here...

  def user_params(params={})
    {
      password: "hello",
      email: "blah@example.com",
      name: "Phil",
      phone_number: "07712345678",
      country_code: "+44"
    }.merge(params)
  end
end
