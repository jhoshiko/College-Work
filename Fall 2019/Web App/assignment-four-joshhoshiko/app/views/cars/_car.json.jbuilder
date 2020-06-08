json.extract! car, :id, :model, :vin, :make_id, :created_at, :updated_at
json.url car_url(car, format: :json)
json.make Make.find_by_id(car.make_id).name
json.parts car.parts.map { |part| part.name}
