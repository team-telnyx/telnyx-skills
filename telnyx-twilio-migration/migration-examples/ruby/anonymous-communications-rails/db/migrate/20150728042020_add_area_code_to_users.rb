class AddAreaCodeToUsers < ActiveRecord::Migration[6.1]
  def change
    add_column :users, :area_code, :string
  end
end
