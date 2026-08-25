# https://leetcode.com/problems/search-in-rotated-sorted-array/
# https://neetcode.io/solutions/search-in-rotated-sorted-array
# Binary Search: Exact Match. Search array indices.

# Ex: [4,5,6,7,0,1,2] # nums[mid] > nums[-1]. pivot = 4. It's really
# [0,1,2,4,5,6,7] rotated left by pivot - 1 = 3

# Just remember flowchart:
# 1. Find mid
# 2. Is num[mid] == target? If yes, return mid.
# 3. Which side is sorted?

# 4. LEFT (nums[l] <= nums[mid])
# 5. Is target in LEFT side? (nums[l] <= target and target <= nums[mid])
# 6. YES: go left
# 7. NO: go right.

# 4. RIGHT
# 5. Is target in RIGHT side? (nums[mid] <= target and target <= nums[r])
# 6. YES: go right
# 7. NO: go left

# Time: O(log n), Space: O(1)
def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid

        if nums[l] <= nums[mid]:    # LEFT side is sorted
            if nums[l] <= target <= nums[mid]:   # target in LEFT side
                r = mid - 1                      # Go LEFT
            else:
                l = mid + 1                      # Go RIGHT

        else:                       # RIGHT side is sorted
            if nums[mid] <= target <= nums[r]:   # target in RIGHT side
                l = mid + 1                      # Go RIGHT
            else:
                r = mid - 1                      # Go LEFT

    return -1

if __name__ == "__main__":
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search([1], 0) == -1
    assert search([3,4,5,6,1,2], 1) == 4
    assert search([3,5,6,0,1,2], 4) == -1
    print("All tests passed!")

#______________________

# We have 3 search spaces:

# 1. Search array indices <=== Can answer be 1 past the array? NO
# Examples:
# - LC 704
# - LC 33
# - LC 153
# Search space:
# 0 ... len(nums)-1
# Answer must be real element.

# 2. Search insertion positions <=== Can answer be 1 past the array? YES
# Examples:
# - LC 35
# - LC 34
# Search space:
# 0 ... len(nums)
# Answer is a boundary.

# 3. Search answer values
# Examples:
# - LC 875
# - LC 1011
# Search space:
# min_possible_answer
# ...
# max_possible_answer
# Examples:
# l = max(weights)
# r = sum(weights)
