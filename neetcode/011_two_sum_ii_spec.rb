# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=problem-list-v2&envId=plakya4j
# two sum ii: Like two sum, but integer array is SORTED. "1-indexed" array: first index is 1, not 0.

# Plan: Use 2 pointers for indices, left and right. Sum nums[left] + nums[right].
# Loop while left < right:
# If sum < target, add 1 to left pointer. sum must be higher!
# If sum > target, subtract 1 from right pointer. sum must be lower!
# Else sum == target, so return [left + 1, right + 1]. We add 1 to each since this is "1-indexed" array.

# Time: O(n), Space: O(1)
def two_sum(nums, target)
  left, right = 0, nums.length - 1
  while left < right
    sum = nums[left] + nums[right]

    if sum < target
      left += 1
    elsif sum > target
      right -= 1
    else
      return [left + 1, right + 1]
    end
  end
end

describe "#two_sum ii" do
  it 'returns indices of two numbers that add up to a specific target' do
    expect(two_sum([2, 7, 11, 15], 9)).to eq [1, 2]
    expect(two_sum([2, 3, 4], 6)).to eq [1, 3]
    expect(two_sum([3, 3], 6)).to eq [1, 2]
    expect(two_sum([-1, 0], -1)).to eq [1, 2]
    expect(two_sum([2, 3, 3, 4], 6)).to eq [1, 4]
  end
end
