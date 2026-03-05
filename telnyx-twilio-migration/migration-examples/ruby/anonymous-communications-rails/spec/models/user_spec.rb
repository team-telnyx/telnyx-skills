require "test_helper"

RSpec.describe User, type: :model do
  fixtures :users

  context "without email" do
    it "is not valid" do
      expect(User.new(user_params(email: nil)).valid?).to be_falsey
    end
  end

  context "with invalid email" do
    it "is not valid" do
     expect(User.new(user_params(email: "blah")).valid?).to be_falsey
    end
  end

  context "with valid email" do
    it "is valid" do
      expect(User.new(user_params).valid?).to be_truthy
    end
  end

  context "with duplicated email" do
    it "is not valid" do
      user = users(:one)
      user2 = User.new(user_params(email: user.email))
      expect(user2.valid?).to be_falsey
    end
  end

  context "with duplicated phone number" do
    it "is not valid" do
      user = users(:one)
      user2 = User.new(user_params(phone_number: user.phone_number))
      expect(user2.valid?).to be_falsey
    end
  end

  context "with invalid password" do
    it "is not valid" do
      expect(User.new(user_params(password: "root")).valid?).to be_falsey
    end
  end

  context "with valid password" do
    it "is valid" do
      expect(User.new(user_params).valid?).to be_truthy
    end
  end

  context "without password" do
    it "is not valid" do
      expect(User.new(user_params(password: nil)).valid?).to be_falsey
    end
  end

  context "without name" do
    it "is not valid" do
      expect(User.new(user_params(name: nil)).valid?).to be_falsey
    end
  end

  context "without country code" do
    it "is not valid" do
      expect(User.new(user_params(country_code: nil)).valid?).to be_falsey
    end
  end

  context "without phone number" do
    it "is not valid" do
      expect(User.new(user_params(phone_number: nil)).valid?).to be_falsey
    end
  end
end
