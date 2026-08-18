# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/
# https://neetcode.io/solutions/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold
# Fixed Sliding Window

# Same answer as https://github.com/rayning0/ctci/blob/master/neetcode/643_maximum_average_subarray_i.py

# Time: O(n), Space:
def numOfSubarrays(arr: list[int], k: int, threshold: int) -> int:
    ans = 0
    window_sum = sum(arr[:k])
    if window_sum / k >= threshold:
        ans += 1

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        if window_sum / k >= threshold:
            ans += 1

    return ans

if __name__ == "__main__":
    assert numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4) == 3
    assert numOfSubarrays([11,13,17,23,29,31,7,5,2,3], 3, 5) == 6
    print("All tests passed!")
