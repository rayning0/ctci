# https://leetcode.com/problems/first-missing-positive/?envType=company&envId=netflix&favoriteSlug=netflix-all
# https://neetcode.io/problems/first-missing-positive/question?list=neetcode250
# Animated solution: https://algomaster.io/animations/dsa/first-missing-positive

# ** EASY TO REMEMBER **
# Time: O(n), Space: O(n)
# def firstMissingPositive(nums: list[int]) -> int:
#     # Collect all positive numbers
#     seen = set()
#     for n in nums:
#         if n > 0:
#             seen.add(n)

#     # Find first missing positive starting from 1
#     res = 1
#     while res in seen:
#         res += 1

#     return res


# Cycle Sort: Use array as hash map. Use in-place bucket.
# For list of length n, answer is always from 1..n + 1
# 1. Rearrange nums in place, with swaps, so:
#   If 1 <= x <= n, stick n in its "home index". nums[x - 1] = x or nums[x] = x + 1.
#
#   x = nums[i]
#   if 1 <= x <= n and nums[x - 1] != x <--- n in wrong position
#       swap nums[i] with nums[x - 1]
#
# Keep doing this until:
# 	•	nums[i] is either:
# 	•	out of range (≤ 0 or > n), or
# 	•	already in the correct spot, or
# 	•	would cause a duplicate swap (same value in target index).
# Then move to next i.

# 2. Scan rearranged nums to find first mismatch
# After cycle sort done:
# 	For i in 0..n - 1:
# 	    If nums[i] != i+1, return i+1.

# If we complete loop and never return:
# 	All nums[i] == i+1, so smallest missing positive is n + 1.


# Time: O(n), Space: O(1)
def firstMissingPositive(nums: list[int]) -> int:
    n = len(nums)

    # 1. Place each number x at index x-1 if possible
    i = 0
    while i < n:
        x = nums[i]  # Correct index for x is x-1
        if 1 <= x <= n and nums[x - 1] != x:
            nums[i], nums[x - 1] = nums[x - 1], nums[i]  # swap them
        else:
            i += 1

    # 2. Scan rearranged nums to find first mismatch
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    # If sorted nums all filled correctly, answer is n + 1
    return n + 1


# print(firstMissingPositive([1, 2, 4, 5, 6, 3, 1]))

if __name__ == "__main__":
    assert firstMissingPositive([1, 2, 0]) == 3
    assert firstMissingPositive([-2, -1, 0]) == 1
    assert firstMissingPositive([3, 4, -1, 1]) == 2
    assert firstMissingPositive([7, 8, 9, 11, 12]) == 1
    assert firstMissingPositive([1, 2, 4, 5, 6, 3, 1]) == 7
    print("All tests passed!")
