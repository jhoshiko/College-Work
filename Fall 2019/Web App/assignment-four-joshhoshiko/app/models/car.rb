class Car < ApplicationRecord
  belongs_to :make
  has_and_belongs_to_many :parts

  validates :model, presence: true, uniqueness: true
  validates :vin, presence: true, uniqueness: true
end
