require 'test_helper'
require 'ostruct'

RSpec.describe SessionsController, type: :controller do

  before(:each) do
    @user = User.create(user_params)
  end

  after(:each) do
    @user.destroy
  end

  describe "GET login" do
    it "returns a 200" do
      get :login
      expect(response).to be_successful
    end
  end

  describe "POST login_attempt" do
    it "posts to login_attempt successfully" do
      post :login_attempt, params: { email: @user.email, login_password: @user.password }
      expect(response).to have_http_status(:redirect)
      expect(response).to redirect_to(home_path)
      expect(session[:user_id]).to eq(@user.id)
    end

    it "posts to login_attempt unsuccessfully" do
      post :login_attempt, params: { email: @user.email, login_password: "blah" }
      expect(response).to be_successful
      expect(response).to render_template(:login)
      expect(session[:user_id]).to be_nil
    end
  end

  describe "GET logout" do
    it "redirects to login" do
      session["user_id"] = @user.id
      assert session["user_id"], "Precondition: user should be logged in"
      get :logout
      expect(response).to have_http_status(:redirect)
      expect(response).to redirect_to(login_path)
      expect(session[:user_id]).to be_nil
    end
  end
end
