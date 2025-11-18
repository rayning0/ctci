# https://leetcode.com/problems/min-stack/?envType=problem-list-v2&envId=plakya4j

# To get O(1) time for `get_min`, we can't loop through anything. We must calculate new min for each new val pushed on stack.

# For each stack element, store a tuple: `[val, current min]`. Each time we push new val on stack, recalculate `current min`. Thus after we pop last element off stack, we still have the last `current min` in the element below that.

# Each function must have O(1) time complexity!
# Time: O(1), Space: O(n)
class MinStack
  def initialize
    @stack = [] # each item on stack is tuple: [val, current min]
  end

  def push(val)
    tuple = if @stack.empty?
                [val, val]
              else
                [val, [get_min, val].min]
              end

    @stack << tuple
  end

  def pop
    @stack.pop
  end

  def top
    @stack.last.first
  end

  def get_min
    @stack.last.last
  end
end

describe '#MinStack class' do
  it 'test its methods' do
    obj = MinStack.new
    obj.push(-2)
    expect(obj.top).to eq -2
    obj.push(0)
    obj.push(-3)
    expect(obj.top).to eq -3
    expect(obj.get_min).to eq -3
    obj.pop
    expect(obj.top).to eq 0
    expect(obj.get_min).to eq -2
  end
end
