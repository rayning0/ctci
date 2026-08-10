# https://leetcode.com/problems/subarray-sum-equals-k/
# https://neetcode.io/solutions/subarray-sum-equals-k

# if prefixSum[j] - prefixSum[i] == k, the contiguous
# subarray from index i+1 to j is one of our target subarrays!

# So for current prefixSum[j], check if we've seen a past_prefix sum before:
# prefixSum[i] == prefixSum[j] - k

# If so, we just found a new subarray whose values sum to k!
# Add number of ways to get this past_prefix sum to our final answer.

# Time: O(n), Space: O(n)
def subarraySum(nums: list[int], k: int) -> int:
    prefix_sums = {0: 1}
    prefix = ans = 0

    for n in nums:
        prefix += n                 # current prefix sum
        past_prefix = prefix - k    # If prefix sum is end of a desired subarray (which sums to k),
            # past_prefix is what last prefix sum SHOULD be before start of this desired subarray.
        ans += prefix_sums.get(past_prefix, 0)  # If we saw past_prefix before, add its freq to final answer. If not, add 0.
        prefix_sums[prefix] = prefix_sums.get(prefix, 0) + 1    # Add 1 to current prefix sum freq

    return ans

if __name__ == "__main__":
    assert subarraySum([5], 5) == 1
    assert subarraySum([1,1,1], 2) == 2
    assert subarraySum([1,2,3], 3) == 2
    # [1, 2], [3] are the subarrays whose sum equals 3.

    assert subarraySum([4,4,4,4,4,4], 4) == 6
    assert subarraySum([2,-1,1,2], 2) == 4
    # subarrays: [2], [2,-1,1], [-1,1,2], [2] all have sum == 2.
    assert subarraySum([1, 0, 4, 1, 2, 3], 5) == 4
    # subarrays: [1, 0, 4], [0, 4, 1], [4, 1], [2, 3] all have sum == 5

    print("All tests passed!")

# nums =      [1, 0, 4, 1, 2, 3], k = 5
# index:       0  1  2  3  4  5
# prefix:      1  1  5  6  8 11
# prefix - k: -4 -4  0  1  3  6

# prefix_sums {
#     0: 1 <-- at index 0, prefix = 1. 1 - k = -4. We've not seen this before. Skip.
#     1: 2 <-- at index 1, prefix = 1. Skip.
#     5: 1 <-- at index 2, prefix = 5. 5 - k = 0, a past_prefix we saw before.
# Thus [1, 0, 4], from past_prefix to prefix, is desired subarray! Add prefix_sums[0] = 1 to ans.
#     6: 1 <-- at index 3, prefix = 6. 6 - k = 1, a past_prefix we saw twice before (at indices 0, 1).
# Thus 2 subarrays [0, 4, 1] and [4, 1] both sum to k. Add prefix_sums[1] = 2 to ans.
#     8: 1 <-- at index 4, prefix = 8. 8 - k = 3, which we've not seen before. Skip.
#    11: 1 <-- at index 5, prefix = 11. 11 - k = 6, a past_prefix we once before (at index 3).
# Thus 1 subarray [2, 3] sums to k. Add prefix_sums[6] = 1 to ans.
# }

# ans: 4 subarrays all sum to k
# [1, 0, 4], [0, 4, 1], [4, 1], [2, 3]
