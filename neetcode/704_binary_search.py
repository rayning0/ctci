# https://leetcode.com/problems/binary-search/?envType=problem-list-v2&envId=plakya4j
# https://neetcode.io/problems/binary-search/question?list=neetcode150
# Binary Search: Exact Match. Search array indices.
# (Data structure must be SORTED (or monotonic).)

# Time: O(log n), Space: O(1)
def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:               # use for EXACT MATCH
        mid = (l + r) // 2

        if nums[mid] == target: # use for EXACT MATCH
            return mid
        elif nums[mid] < target:
            l = mid + 1     # do NOT use l +=1, which is O(n). mid eliminates half of search space, O(log n).
        else:
            r = mid - 1

    return -1

if __name__ == "__main__":
    assert search([5], 5) == 0
    assert search([-1, 0, 3, 5, 9], 9) == 4  # tricky for odd size
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert search([-1, 0, 2, 4, 6, 8], 4) == 3
    assert search([-1, 0, 2, 4, 6, 8], 3) == -1
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
