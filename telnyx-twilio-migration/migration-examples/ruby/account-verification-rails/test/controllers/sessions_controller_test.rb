require 'test_helper'
require 'ostruct'

class SessionsControllerTest < ActionController::TestCase
  setup do
    @user = User.create(user_params(authy_id: "123"))
  end

  teardown do
    @user.destroy
  end

  test "should get new" do
    skip
    get :new
    assert_response :success
    assert assigns(:user)
  end

  test "should post to create successfully" do
    skip
    Authy::API.expects(:request_sms).with(id: "123").once
    post :create, email: @user.email, password: user_params[:password]
    assert_response :redirect
    assert_redirected_to sessions_two_factor_path
    assert_equal @user.id, session["pre_2fa_auth_user_id"]
  end

  test "should post to create unsuccessfully" do
    skip
    Authy::API.expects(:request_sms).never
    post :create, email: @user.email, password: "blah"
    assert_response :success
    assert_template :new
    assert_nil session["pre_2fa_auth_user_id"]
  end

  test "should post to verify successfully" do
    skip
    session["pre_2fa_auth_user_id"] = @user.id
    verify = OpenStruct.new(:ok? => true)
    Authy::API.expects(:verify).with(
      id: @user.authy_id,
      token: '123456'
    ).once.returns(verify)
    post :verify, :token => '123456'
    assert_response :redirect
    assert_redirected_to account_path
    assert_nil session["pre_2fa_auth_user_id"]
    assert_equal session[:user_id], @user.id
  end

  test "should post to verify unsuccessfully" do
    skip
    session["pre_2fa_auth_user_id"] = @user.id
    verify = OpenStruct.new(:ok? => false)
    Authy::API.expects(:verify).with(
      id: @user.authy_id,
      token: '123456'
    ).once.returns(verify)
    post :verify, :token => '123456'
    assert_response :success
    assert_template :two_factor
  end

  test "should get to two_factor when a pre_2fa_auth_user_id in session" do
    skip
    session["pre_2fa_auth_user_id"] = @user.id
    get :two_factor
    assert_response :success
    assert_template :two_factor
  end

  test "get to two_factor should redirect without a pre_2fa_auth_user_id in session" do
    skip
    session["pre_2fa_auth_user_id"] = nil
    get :two_factor
    assert_response :redirect
    assert_redirected_to new_session_path
  end

  test "should get destroy" do
    skip
    session["user_id"] = @user.id
    assert session["user_id"], "Precondition: user should be logged in"
    get :destroy
    assert_response :redirect
    assert_redirected_to root_path
    assert_nil session["user_id"]
  end
end
