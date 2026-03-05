class User < ActiveRecord::Base
  has_secure_password

  validates :email,  presence: true, format: { with: /\A.+@.+$\Z/ }, uniqueness: true
  validates :name, presence: true
  validates :country_code, presence: true
  validates :phone_number, presence: true, uniqueness: true
  validates_length_of :password, in: 6..20, on: :create

  has_many :vacation_properties
  has_many :reservations, through: :vacation_properties

  after_create :save_join_phone_number!

  def send_message_via_sms(message, from_number = ENV['TELNYX_PHONE_NUMBER'])
    Telnyx.api_key = ENV['TELNYX_API_KEY']
    Telnyx::Message.create(
      from: from_number,
      to: self.phone_number,
      text: message,
      messaging_profile_id: ENV['TELNYX_MESSAGING_PROFILE_ID']
    )
  end

  def check_for_reservations_pending
    if pending_reservation
      pending_reservation.notify_host(true)
    end
  end

  def pending_reservation
    self.reservations.pending.first
  end

  def pending_reservations
    self.reservations.pending
  end

  private

  # No reason to save phone number without the area_code or country_code, it's what telnyx & ActiveRecord expect
  def save_join_phone_number!
    self.update!(phone_number: "#{self.country_code}#{self.area_code}#{self.phone_number}")
  end

end
