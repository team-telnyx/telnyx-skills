require 'test_helper'

RSpec.describe MainController, type: :controller do
  describe "GET index" do
    it "returns a 200 response" do
      get :index
      expect(response).to be_successful
    end
  end
end
