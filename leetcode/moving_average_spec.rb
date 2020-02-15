# https://leetcode.com/problems/moving-average-from-data-stream/

class MovingAverage
  def initialize(size)
    @size = size

    # use class variable since next instances of m must remember arr
    @@arr = []
  end

  def next(val)
    @@arr.empty? ? @@arr = [val] : @@arr << val
    @@arr.shift if @@arr.size > @size
    sum = @@arr.reduce(:+).to_f
    sum / @@arr.size
  end
end

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage.new(size)
# param_1 = obj.next(val)

describe "#MovingAverage" do
  m = MovingAverage.new(3)

  it 'returns moving average for window size 3, as we add more data' do
    expect(m.next(1)).to eq 1
    expect(m.next(10)).to eq 5.5
    expect(m.next(3)).to eq 14.0 / 3
    expect(m.next(5)).to eq 6
  end
end
