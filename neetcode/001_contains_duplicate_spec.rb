# https://leetcode.com/problems/contains-duplicate/description/?envType=problem-list-v2&envId=plakya4j

# Plan: Use hash to track freq of each num. If we've stored num before in hash, return true.
# If we loop to end of array without seeing num, return false.
# Time: O(n), Space: O(n)
def contains_duplicate(nums)
  hash = {}
  nums.each do |num|
    return true if hash[num]
    hash[num] = true
  end
  false
end

describe "#contains_duplicate" do
  it "returns true if array contains any duplicates, false otherwise" do
    expect(contains_duplicate([1, 2, 3, 1])).to eq(true)
    expect(contains_duplicate([1, 2, 3, 4])).to eq(false)
    expect(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])).to eq(true)
  end
end
