# https://leetcode.com/problems/subarray-sums-divisible-by-k/description/
# https://neetcode.io/solutions/subarray-sums-divisible-by-k

# Like "LC #560: Subarray Sum Equals K"
# https://github.com/rayning0/ctci/blob/master/neetcode/560_subarray_sum_equals_k.py

# If prefixSum[j] - prefixSum[i] == ck (where c is integer), the contiguous
# subarray from index i+1 to j is a target subarray!
# (prefixSum[j] - prefixSum[i]) % k == 0.

# Thus: If 2 prefix sums have the same "mod k" value (or REMAINDER when divided by k),
# their difference is divisible by k! <-- KEY INSIGHT

# Time: O(n), Space: O(k)
def subarraysDivByK(nums: list[int], k: int) -> int:
    prefix_sums = {0: 1}
    prefix = ans = 0

    for n in nums:
        prefix += n
        remainder = prefix % k
        ans += prefix_sums.get(remainder, 0)
        prefix_sums[remainder] = prefix_sums.get(remainder, 0) + 1

    return ans

if __name__ == "__main__":
    assert subarraysDivByK([4,5,0,-2,-3,1], 5) == 7
# 7 subarrays have a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [0], [5, 0, -2, -3], [0, -2, -3], [-2, -3]
    assert subarraysDivByK([5], 9) == 0
    print("All tests passed!")

# nums =                        [4,   5,  0,  -2, -3, 1], k = 5
# index:                     -1  0    1   2    3   4  5
# prefix:                        4    9   9    7   4  5
# remainder = prefix % k:     0  4    4   4    2   4  0

# prefix_sums = {
#     0: 2 <-- at index 5, remainder = 0. We saw this at index -1 (default).
# Thus [4,5,0,-2,-3,1], from index -1 to 5, is target subarray. Add prefix_sums[0] = 1 to ans.
#     2: 1 <-- at index 3, remainder = 2. This is new. Skip.
#     4: 4 <-- at index 0, remainder = 4. This is new. Skip.
#          <-- at index 1, remainder = 4. We saw this before at index 0.
# Thus [5], from index 1 only, is a target subarray.            Add prefix_sums[4] = 1 to ans.
#          <-- at index 2, remainder = 4. We saw this at index 0 and 1.
# Thus [5,0] and [0] are target subarrays.                      Add prefix_sums[4] = 2 to ans.
#          <-- at index 4, remainder = 4. We saw this at index 0, 1, and 2.
# Thus [5,0,-2,-3], [0,-2,-3], & [-2,-3] are target subarrays.  Add prefix_sums[4] = 3 to ans.
# }

# ans = 1 + 1 + 2 + 3 = 7 subarrays are all divisible by k
