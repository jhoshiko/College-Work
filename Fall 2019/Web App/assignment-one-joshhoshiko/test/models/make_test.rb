require 'test_helper'

class MakeTest < ActiveSupport::TestCase
  test "for empty name" do
    s = Make.create({:name => "", :country => "United States"})
    refute s.valid?
    refute s.save
  end

  test "for empty country" do
    s = Make.create({:name => "Saab", :country => ""})
    refute s.valid?
    refute s.save
  end

  test "for non-unique make" do
    s = Make.create({:name => "Saab", :country => "Sweden"})
    r = Make.create({:name => "Saab", :country => "Sweden"})
    assert s.valid?
    assert s.save
    refute r.valid?
    refute r.save
  end
end
