# https://leetcode.com/problems/binary-subarrays-with-sum/description/
# https://neetcode.io/solutions/binary-subarrays-with-sum

# 1. Prefix Sum + Hashmap. Same solution as
# https://github.com/rayning0/ctci/blob/master/neetcode/560_subarray_sum_equals_k.py
# Time: O(n), Space: O(n)
# def numSubarraysWithSum(nums: list[int], goal: int) -> int:
#     prefix_sums = {0: 1}
#     prefix = ans = 0

#     for n in nums:
#         prefix += n
#         past_prefix = prefix - goal
#         ans += prefix_sums.get(past_prefix, 0)
#         prefix_sums[prefix] = prefix_sums.get(prefix, 0) + 1

#     return ans

# 2. Sliding Window (Best)
# Time: O(n), Space: O(1)
def numSubarraysWithSum(nums: list[int], goal: int) -> int:

if __name__ == "__main__":
    assert numSubarraysWithSum([1,0,1,0,1], 2) == 4
    assert numSubarraysWithSum([0,0,0,0,0], 0) == 15
    print("All tests passed!")
