class VacationProperty < ActiveRecord::Base
  belongs_to :user # host
  has_many :reservations
  has_many :users, through: :reservations #guests
end
