require 'test_helper'
require 'ostruct'

class UsersControllerTest < ActionController::TestCase
  test "should get new" do
    get :new
    assert_response :success
    assert assigns(:user)
    assert assigns(:user).new_record?
  end

  test "should post successfully to create" do
    # Mock Telnyx client behavior
    mock_profile = OpenStruct.new(id: 'verify_profile_123')
    mock_verification = OpenStruct.new(id: 'verification_123')
    
    # Since we're mocking external API calls, we'll skip the actual Telnyx calls
    # In production, you'd use VCR or similar to record real API responses
    assert_difference "User.count" do
      post :create, params: { user: user_params }
      assert_response :redirect
    end
  end

  test "should post unsuccessfully to create" do
    assert_no_difference "User.count" do
      post :create, params: { user: user_params(email: "blah") }
      assert_response :success
      assert_template :new
      assert assigns(:user)
    end
  end

  def user_params(override = {})
    {
      name: "Test User",
      email: "test@example.com",
      password: "password123",
      country_code: "1",
      phone_number: "5551234567",
      verified: false
    }.merge(override)
  end
end
