# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Video explanation: https://www.youtube.com/watch?v=QdVrY3stDD4
# Runtime: 36 ms, faster than 61.33% of Ruby online submissions for Search in Rotated Sorted Array.
# Memory Usage: 9.6 MB, less than 100.00% of Ruby online submissions for Search in Rotated Sorted Array.

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}

# O(log n) time complexity. O(1) space complexity.
def search(nums, target)
    return -1 if nums.size == 0
    left = 0
    right = nums.size - 1

    # find index of smallest element
    while left < right do
        mid = (left + right) / 2
        if nums[mid] > nums[right]
            left = mid + 1
        else
            right = mid
        end
    end
    # puts "smallest element: #{left}"

    if target.between?(nums[left], nums[nums.size - 1])
        right = nums.size - 1 # search to right of smallest element
    else
        right = left          # search to left of smallest element
        left = 0
    end

    # normal binary search
    while left <= right do
        mid = (left + right) / 2
        if target == nums[mid]
            return mid
        elsif target > nums[mid]
            left = mid + 1
        else
            right = mid - 1
        end
    end

    -1
end

describe '#search' do
  it 'finds index of target value in rotated sorted array' do
    expect(search([], 0)).to eq -1
    expect(search([3,1], 3)).to eq 0
    expect(search([5,1,3], 5)).to eq 0
    expect(search([4,5,6,7,0,1,2], 0)).to eq 4
    expect(search([4,5,6,7,0,1,2], 3)).to eq -1
  end
end
