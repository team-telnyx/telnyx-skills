require 'test_helper'

class AccountsControllerTest < ActionController::TestCase
  test "should redirect when not logged in" do
    skip
    get :show
    assert_response :redirect
    assert_redirected_to new_session_path
  end

  test "should succeed when logged in" do
    skip
    session["user_id"] = users(:one).id
    get :show
    assert_response :success
    assert_equal assigns(:user), users(:one)
  end
end
