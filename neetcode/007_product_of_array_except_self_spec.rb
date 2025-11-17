# https://leetcode.com/problems/product-of-array-except-self/?envType=problem-list-v2&envId=plakya4j
# Use prefix and postfix products.
# Time: O(n), Space: O(n)

# Ex: nums = [5, 6, 2, 10]

#         (1)       5,             6,         2,       10,      (1)
# prefix:           1            1*5=5   1*5*6=30  1*5*6*2=60      =  [1,  5, 30, 60]
# postfix:       6*2*10*1=120  2*10*1=20   10*1        1           = [120, 20, 1,  1]
# ________________________________________________________
# prefix * postfix: 1*120=120   5*20=100 30*10=300   60*1=60
# Ans: [120, 100, 300, 60]

def product_except_self(nums)
  size = nums.size
  prefix, postfix = Array.new(size, 1), Array.new(size, 1)
  leftprod, rtprod = 1, 1

  (1..size - 1).each do |i|
    leftprod *= nums[i - 1] # product of all nums to LEFT of nums[i]
    prefix[i] = leftprod
  end

  (size - 2).downto(0) do |i|
    rtprod *= nums[i + 1] # product of all nums to RIGHT of nums[i]
    postfix[i] = rtprod
  end

  # Imperative style:

  # ans = []
  # size.times do |i|
  #   ans << prefix[i] * postfix[i]
  # end
  # ans

  # Functional style:
  size.times.reduce([]) { |acc, i| acc << prefix[i] * postfix[i] }
end

describe "#product_except_self" do
  it 'gets product of all nums in array except num at that index' do
    expect(product_except_self([5, 6, 2, 10])).to eq [120,100,300,60]
    expect(product_except_self([1,2,3,4])).to eq [24,12,8,6]
    expect(product_except_self([-1, 1, 0, -3, 3])).to eq [0,0,9,0,0]
  end
end
