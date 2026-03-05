require 'test_helper'
require 'ostruct'

RSpec.describe UsersController, type: :controller do
  describe "GET new" do
    it "has new empty user" do
      get :new
      expect(response).to be_successful
      expect(assigns(:user)).to_not be_nil
      expect(assigns(:user).new_record?).to be(true)
    end
  end

  describe "POST create" do
    context "when params are valid" do
      it "creates a user" do
        expect do
          post :create, params: { user: user_params }
          expect(response).to have_http_status(:redirect)
          expect(response).to redirect_to(home_path)
        end.to change { User.count }
      end
    end

    context "when params are not valid" do
      it "does not create a user" do
        expect do
          post :create, params: { user: user_params(email: "blah") }
          expect(response).to be_successful
          expect(response).to render_template(:new)
          expect(assigns(:user)).to_not be_nil
        end.to_not change { User.count }
      end
    end
  end
end
