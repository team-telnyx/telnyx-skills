require "test_helper"

class UserTest < ActiveSupport::TestCase
  test "user requires email" do
    assert !User.new(user_params(email: nil)).valid?
  end

  test "email looks like an email" do
    assert !User.new(user_params(email: "blah")).valid?
    assert User.new(user_params).valid?
  end

  test "email should be unique" do
    user = users(:one)
    user2 = User.new(user_params(email: user.email))
    assert !user2.valid?
  end

  test "user requires password" do
    assert !User.new(user_params(password: nil)).valid?
  end

  test "user requires name" do
    assert !User.new(user_params(name: nil)).valid?
  end

  test "user requires country code" do
    assert !User.new(user_params(country_code: nil)).valid?
  end

  test "user requires phone number" do
    assert !User.new(user_params(phone_number: nil)).valid?
  end
end
