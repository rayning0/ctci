# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=problem-list-v2&envId=plakya4j
# use sliding window

# Time: O(n), Space: O(1)
def max_profit(prices)
  return 0 if prices.size == 1

  l, r = 0, 1
  max_profit = 0

  while r < prices.size
    if prices[l] < prices[r]
      profit = prices[r] - prices[l]
      max_profit = [max_profit, profit].max
    else
      l = r
    end

    r += 1
  end

  max_profit
end

# Simpler
# def max_profit(prices)
#   min_price = prices[0]
#   max_profit = 0

#   prices.each do |price|
#     min_price = [min_price, price].min
#     profit = price - min_price
#     max_profit = [max_profit, profit].max
#   end

#   max_profit
# end

describe "#buying stock" do
  it 'gets product of all nums in array except num at that index' do
    expect(max_profit([2,1,4])).to eq 3
    expect(max_profit([7,1,5,3,6,4])).to eq 5
    expect(max_profit([7,6,4,3,1])).to eq 0
    expect(max_profit([10,1,5,6,7,1])).to eq 6
    expect(max_profit([10,8,7,5,2])).to eq 0
  end
end
