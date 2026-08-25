# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
# https://neetcode.io/solutions/find-minimum-in-rotated-sorted-array
# Binary Search: Lower Bound on Elements. Search array indices.

# Basically: Find pivot value. Keep shrinking search interval until only min is left.

# INSIGHT: If nums[mid] > nums[r], min must be to the RIGHT of mid.
# Otherwise, mid could already be min, so keep it and search left (r = mid).

# Time: O(log n), Space: O(1)
def findMin(nums: list[int]) -> int:
    l, r = 0, len(nums) - 1         # We search on actual elements, hence "r = len(nums) - 1"

    while l < r:                    # We seek lower bound, hence "while l < r"
        mid = (l + r) // 2

        if nums[mid] > nums[r]:     # Min must be in RIGHT side
            l = mid + 1             # Go RIGHT
        else:                       # Min must be mid or on LEFT side
            r = mid                 # Stay at mid or go LEFT

    return nums[l]

if __name__ == "__main__":
    assert findMin([3,4,5,1,2]) == 1
    assert findMin([4,5,6,7,0,1,2]) == 0
    assert findMin([11,13,15,17]) == 11
    assert findMin([3,4,5,6,1,2]) == 1
    assert findMin([4,5,0,1,2,3]) == 0
    assert findMin([4,5,6,7]) == 4
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
