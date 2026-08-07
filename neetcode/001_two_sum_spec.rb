
# https://leetcode.com/problems/two-sum/description/?envType=problem-list-v2&envId=plakya4j

# Make hash with key = num, val = its index. So [2, 4] makes hash {2 => 0, 4 => 1}
# Loop thru array and find diff of current element = target - nums[i].
# Did we already see diff in hash? If seen[diff] exists, return [seen[diff], i]
# Time: O(n), Space: O(n)
def two_sum(nums, target)
  seen = {}
  nums.each_with_index do |num, i|
    diff = target - num
    if seen[diff]
      return [seen[diff], i] # always return seen[diff] index, then i, in this order. seen[diff] will always be < i.
    end
    seen[num] = i
  end

  [] # no answer
end

describe "#two_sum" do
  it 'returns indices of two numbers that add up to a specific target' do
    expect(two_sum([2, 4, 7, 11, 15], 9)).to eq [0, 2]
    expect(two_sum([2, 7, 11, 15], 9)).to eq [0, 1]
    expect(two_sum([3, 3], 6)).to eq [0, 1]
    expect(two_sum([3, 2, 4], 6)).to eq [1, 2]
    expect(two_sum([5, 3], 2)).to eq []
  end
end

# Ex: nums = [2, 4, 7, 11, 15],  target = 9
# seen = {2 => 0, 4 => 1, 7 => 2, 11 => 3, 15 => 4}
# i = 0
# if seen[9-2] exists, return [seen[diff], i] = [0, 2]

# nums = [3, 3], target = 6
# i = 0
# seen = {3 => 0}
# i = 1. Was 3 seen? Yes, at i = 0, Ans: [0, 1]
