# https://leetcode.com/problems/binary-subarrays-with-sum/description/
# https://neetcode.io/solutions/binary-subarrays-with-sum

# 1. Prefix Sum + Hashmap. Same solution as
# https://github.com/rayning0/ctci/blob/master/neetcode/560_subarray_sum_equals_k.py
# Time: O(n), Space: O(n)
def numSubarraysWithSum(nums: list[int], goal: int) -> int:
    prefix_sums = {0: 1}
    prefix = ans = 0

    for n in nums:
        prefix += n
        past_prefix = prefix - goal
        ans += prefix_sums.get(past_prefix, 0)
        prefix_sums[prefix] = prefix_sums.get(prefix, 0) + 1

    return ans

# 2. Variable Sliding Window (Best!) Use l + r pointers.

# TRICK! count(goal) = count(<= goal) - count(<= (goal - 1))
# Ex: count(all subarrays that sum to 2) = count(all subarrays that sum to 1 or 2) - count(all subarrays that sum to 1)

# Time: O(n), Space: O(1)
def numSubarraysWithSum(nums: list[int], goal: int) -> int:

    # count subarrays that sum to <= goal
    def count(goal):
        ans = l = sum = 0

    # This is binary array: n = 0 or 1.
    # Since we never have negative elements, we have 0 ways to sum to a negative goal.
        if goal < 0:
            return 0

        for r in range(len(nums)):
            sum += nums[r]

            # while sum > goal, shrink sliding window by left element
            while sum > goal:
                sum -= nums[l]
                l += 1

            # # of valid subarrays (sum to <= goal) that end at index r = length of sliding window = r - l + 1
            # Ex: nums = [1,0,1,0,1], goal = 2
            # For sliding window ending at index r = 2, it has 3 valid subarrays. 3 = r - l + 1:
            # [1,0,1]  start at index 0
            #   [0,1]  start at index 1
            #     [1]  start at index 2
            ans += r - l + 1

        return ans

    return count(goal) - count(goal - 1)

if __name__ == "__main__":
    assert numSubarraysWithSum([1,0,1,0,1], 2) == 4
    assert numSubarraysWithSum([0,0,0,0,0], 0) == 15
    print("All tests passed!")

# Ex: nums = [1, 0, 1, 0, 1], goal = 2

# count(2) counts subarrays whose sum <= 2.

# Initial state:

# l = 0
# sum = 0
# ans = 0
# r = 0

# Add nums[0] = 1:

# sum = 1
# l = 0
# sum <= 2, so no shrinking.

# Valid subarrays ending at r = 0:

# start 0: [1]       sum = 1

# r - l + 1 = 0 - 0 + 1 = 1
# ans = 1
# r = 1

# Add nums[1] = 0:

# sum = 1
# l = 0
# Valid subarrays ending at r = 1:

# start 0: [1, 0]    sum = 1
# start 1:    [0]    sum = 0

# r - l + 1 = 1 - 0 + 1 = 2
# ans = 1 + 2 = 3
# r = 2

# Add nums[2] = 1:

# sum = 2
# l = 0
# sum <= 2, so no shrinking.

# Valid subarrays ending at r = 2:

# start 0: [1, 0, 1]  sum = 2
# start 1:    [0, 1]  sum = 1
# start 2:       [1]  sum = 1

# r - l + 1 = 2 - 0 + 1 = 3
# ans = 3 + 3 = 6
# r = 3

# Add nums[3] = 0:

# sum = 2
# l = 0
# Valid subarrays ending at r = 3:

# start 0: [1, 0, 1, 0]  sum = 2
# start 1:    [0, 1, 0]  sum = 1
# start 2:       [1, 0]  sum = 1
# start 3:          [0]  sum = 0

# r - l + 1 = 3 - 0 + 1 = 4
# ans = 6 + 4 = 10
# r = 4

# Add nums[4] = 1:

# sum = 3
# l = 0
# Now sum > goal, so shrink from the left.

# Remove nums[0] = 1:

# sum = 2
# l = 1
# Now sliding window is:

# nums[1:5] = [0, 1, 0, 1]
# Valid subarrays ending at r = 4:

# start 1: [0, 1, 0, 1]  sum = 2
# start 2:    [1, 0, 1]  sum = 2
# start 3:       [0, 1]  sum = 1
# start 4:          [1]  sum = 1
# The subarray starting at 0 is excluded:

# [1, 0, 1, 0, 1]  sum = 3

# r - l + 1 = 4 - 1 + 1 = 4
# ans = 10 + 4 = 14

# Therefore:

# count(2) = 1 + 2 + 3 + 4 + 4 = 14
# There are 14 subarrays with sum <= 2.

# Thus:

# count(1) = 10
# count(2) = 14

# numSubarraysWithSum(..., 2) = count(2) - count(1)
#                             = 14 - 10
#                             = 4

# The 4 subarrays with sum exactly 2 are:

# [1,0,1]       # indices 0..2
# [1,0,1,0]     # indices 0..3
# [0,1,0,1]     # indices 1..4
# [1,0,1]       # indices 2..4
