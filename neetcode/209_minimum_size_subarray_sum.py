# https://leetcode.com/problems/minimum-size-subarray-sum/description/
# https://neetcode.io/solutions/minimum-size-subarray-sum
# Variable Sliding Window

# When we hit sum >= target, shrink left window
# Time: O(n), Space: O(1)
def minSubArrayLen(target: int, nums: list[int]) -> int:
    l = sum = 0
    min_length = float("inf")

    for r in range(len(nums)):
        sum += nums[r]

        while sum >= target:
            min_length = min(min_length, r - l + 1)
            sum -= nums[l]
            l += 1

    min_length = 0 if min_length == float("inf") else min_length

    return min_length

if __name__ == "__main__":
    assert minSubArrayLen(7, [2,3,1,2,4,3]) == 2
    assert minSubArrayLen(4, [1,4,4]) == 1
    assert minSubArrayLen(11, [1,1,1,1,1,1,1,1]) == 0
    assert minSubArrayLen(10, [2,1,5,1,5,3]) == 3
    assert minSubArrayLen(5, [1,2,1]) == 0
    print("All tests passed!")
