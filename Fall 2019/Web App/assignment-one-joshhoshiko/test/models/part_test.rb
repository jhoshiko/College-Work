require 'test_helper'

class PartTest < ActiveSupport::TestCase
  test "for empty name" do
    s = Car.create({:name => ""})
    refute s.valid?
    refute s.save
  end

  test "for non-unique part" do
    s = Part.create({:name => "Exhaust"})
    r = Part.create({:name => "Exhaust"})
    assert s.valid?
    assert s.save
    refute r.valid?
    refute r.save
  end

end
