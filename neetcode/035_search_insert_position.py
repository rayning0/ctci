# https://leetcode.com/problems/search-insert-position/
# https://neetcode.io/solutions/search-insert-position
# Binary Search: Lower Bound. Search insertion positions.

# "return index if target found. If not, return index where it would be if INSERTED in order."

# Time: O(log n), Space: O(1)
def searchInsert(nums: list[int], target: int) -> int:
    l, r = 0, len(nums)

    while l < r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        else:             # <--- nums[mid] >= target
            r = mid

    return l              # <--- when l == r

if __name__ == "__main__":
    assert searchInsert([1,3,5,6], 5) == 2
    assert searchInsert([1,3,5,6], 2) == 1
    assert searchInsert([1,3,5,6], 7) == 4
    assert searchInsert([-1, 0, 2, 4, 6, 8], 5) == 4
    assert searchInsert([-1, 0, 2, 4, 6, 8], 10) == 6
    print("All tests passed!")

# For questions like:
# "Find FIRST value that meets a condition."
# "Find first place I can legally INSERT target."
# "Keep any value that could still be the answer."
# "What's the smallest capacity that works?"

# Use LOWER BOUND pattern instead!
# Most interview binary search problems are LOWER BOUND, not EXACT MATCH.

# "Lower Bound": first index when nums[i] >= target.
# Instead of exact match, LOWER BOUND says:
# “This could be the answer, but maybe there’s another valid answer to its left.”
# So it: 1) Saves current answer. 2) Keeps searching on its left.

# l, r = 0, len(nums)

# while l < r:
#     mid = (l + r) // 2
#     if nums[mid] < target:
#         l = mid + 1
#     else:                   <---- nums[mid] >= target
#         r = mid

# return l                    <--- when l == r

# ---------------------------------------------------
# Related problem, but exact same answer!

# "First Insertion Position (with Duplicates)":
# Given sorted array of integers (may contain duplicates) and target value,
# return the first index where nums[i] >= target.

def firstInsert(nums: list[int], target: int) -> int:
    l, r = 0, len(nums)

    while l < r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid

    return l

if __name__ == "__main__":
    assert firstInsert([1, 2, 2, 2, 3, 5, 6], 2) == 1
    assert firstInsert([1, 2, 2, 2, 3, 5, 6], 4) == 5
    assert firstInsert([1, 2, 2, 2, 3, 5, 6], 7) == 7
    assert firstInsert([2, 2, 2, 2], 2) == 0
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
