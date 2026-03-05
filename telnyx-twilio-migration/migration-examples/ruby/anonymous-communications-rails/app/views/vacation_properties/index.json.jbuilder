json.array!(@vacation_properties) do |vacation_property|
  json.extract! vacation_property, :id, :description, :image_url
  json.url vacation_property_url(vacation_property, format: :json)
end
