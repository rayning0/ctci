# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
# https://neetcode.io/solutions/find-first-and-last-position-of-element-in-sorted-array
# Binary Search: Lower + Upper Bound. Search insertion positions.

# Lower bound(target): first index whose value is >= target
# Upper bound(target): first index whose value is > target

# lower_bound(x) = first value >= x
#                = count of values < x
# upper_bound(x) = first value > x
#                = count of values <= x

# Remember, any index in list = # of items that come before it.

# EXAMPLE:
# nums   = [1, 2, 2, 2, 4]
# index     0  1  2  3  4

# For target = 2:
# lower_bound(2) = 1   # first value >= 2
# upper_bound(2) = 4   # first value > 2

# # Lower bound(target): first nums[mid] >= target
# if nums[mid] >= target:
#     r = mid
# else:
#     l = mid + 1

# # Upper bound(target): first nums[mid] > target
# if nums[mid] > target:
#     r = mid
# else:
#     l = mid + 1

# Time: O(log n), Space: O(1)
def searchRange(nums: list[int], target: int) -> list[int]:
    # LOWER BOUND(target)
    # First index whose value >= target
    l, r = 0, len(nums)

    while l < r:
        mid = (l + r) // 2
        if nums[mid] >= target:
            r = mid
        else:
            l = mid + 1
    first = l

    # If target NOT in array. Either:
    # 1. We ran past end of array: first == len(nums)
    # 2. nums[first] != target
    if first == len(nums) or nums[first] != target:
        return [-1, -1]

    # UPPER BOUND(target) =  First index whose value > target = LOWER BOUND(target + 1) = l
    # Since upper bound points to first value > target, last target is 1 index before it, so last = l - 1.
    l, r = 0, len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid] > target:  # OR nums[mid] >= target + 1
            r = mid
        else:
            l = mid + 1
    last = l - 1

    return [first, last]

if __name__ == "__main__":
    assert searchRange([5,7,7,8,8,10], 8) == [3,4]
    assert searchRange([5,7,7,8,8,10], 6) == [-1,-1]
    assert searchRange([], 0) == [-1,-1]
    assert searchRange([1], 1) == [0,0]
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
