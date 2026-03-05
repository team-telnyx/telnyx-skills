class CreateReservations < ActiveRecord::Migration[6.1]
  def change
    create_table :reservations do |t|
      t.string :name
      t.string :guest_phone
      t.integer :status, default: 0
      t.text :message
      t.belongs_to :vacation_property, index:true

      t.timestamps null: false
    end
  end
end
