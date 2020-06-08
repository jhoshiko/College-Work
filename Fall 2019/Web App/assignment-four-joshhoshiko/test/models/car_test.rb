require 'test_helper'

class CarTest < ActiveSupport::TestCase
  test "for empty model" do
    s = Car.create({:model => "", :vin => "1234"})
    refute s.valid?
    refute s.save
  end

  test "for empty vin" do
    s = Car.create({:model => "Car", :vin => ""})
    refute s.valid?
    refute s.save
  end

  test "for non-unique car" do
    s = Car.create({:model => "Car", :vin => "1234"})
    r = Car.create({:model => "Car", :vin => "1234"})
    assert s.valid?
    assert s.save
    refute r.valid?
    refute r.save
  end

end
