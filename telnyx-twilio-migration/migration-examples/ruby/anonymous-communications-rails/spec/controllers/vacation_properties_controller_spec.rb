require 'test_helper'

RSpec.describe VacationPropertiesController, type: :controller do
  fixtures :vacation_properties

  before(:each) do
    @vacation_property = vacation_properties(:one)
    @user = User.create(user_params)
    # Need to login user to view properties
    session[:user_id] = @user.id
  end

  after(:each) do
    @user.destroy
  end

  describe "GET index" do
    it "has vacation properties" do
      get :index
      expect(response).to be_successful
      expect(assigns(:vacation_properties)).to_not be_nil
    end
  end

  describe "GET new" do
    it "has a new empty vacation property" do
      get :new
      expect(response).to be_successful
      expect(assigns(:vacation_property)).to_not be_nil
      expect(assigns(:vacation_property).new_record?).to be(true)
    end
  end

  describe "POST create" do
    it "creates a new vacation property" do
      expect do
        session[:user_id] = @user.id
        post :create, params: { vacation_property: { description: @vacation_property.description, image_url: @vacation_property.image_url } }
      end.to change { VacationProperty.count }
      expect(response).to redirect_to(vacation_property_path(assigns(:vacation_property)))
    end
  end

  describe "GET show" do
    it "returns a 200" do
      get :show, params: { id: @vacation_property }
      expect(response).to be_successful
    end
  end

  describe "GET edit" do
    it "returns a 200" do
      get :edit, params: { id: @vacation_property }
      expect(response).to be_successful
    end
  end

  describe "PATCH vacation_property" do
    it "updates and redirects" do
      patch :update, params: { id: @vacation_property, vacation_property: { description: @vacation_property.description, image_url: @vacation_property.image_url } }
      expect(response).to redirect_to(vacation_property_path(assigns(:vacation_property)))
    end
  end

  describe "DELETE vacation_property" do
    it "destroys and redirects" do
      expect do
        delete :destroy, params: { id: @vacation_property }
      end.to change { VacationProperty.count }.by(-1)
  
      expect(response).to redirect_to(vacation_properties_path)
    end
  end
end
