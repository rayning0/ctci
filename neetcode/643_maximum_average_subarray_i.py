# https://leetcode.com/problems/maximum-average-subarray-i/description/
# https://algo.monster/liteproblems/643
# Sliding Window

# Find subarray with max sum:
# - Don't loop through sum(nums[i:i + k]). Too slow!
# - With sliding window, instead of recalculating whole sum in each loop, just update current sum:
#   - Add new element that just entered window: nums[i]
#   - Subtract element that just left sliding window: nums[i - k]

# Time: O(n), Space: O(1)
def findMaxAverage(nums: list[int], k: int) -> float:
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        # WRONG! Too slow. Times out in LeetCode, since it does redundant sums
        # window_sum = sum(nums[i:i + k])

        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    # wait till end to divide by k
    return max_sum / k


if __name__ == "__main__":
    assert findMaxAverage([-1], 1) == -1.00000
    assert findMaxAverage([1,12,-5,-6,50,3], 4) == 12.75000
    assert findMaxAverage([5], 1) == 5.00000
    assert findMaxAverage([5, 2, -1, 3, 7], 3) == 3.0
    print("All tests passed!")
