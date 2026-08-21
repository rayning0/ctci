# https://leetcode.com/problems/max-consecutive-ones-iii/
# https://neetcode.io/problems/max-consecutive-ones-iii/solution
# Variable Sliding Window

# INSIGHT: A sliding window may have at most k zeros!
# As we expand window's right edge, reduce k by 1 for each zero seen. It's one less zero we can flip to one.
# When k < 0, the window has too many zeros, so shrink it from left until the window is valid again.
# As we shrink window, if old left element was zero, add 1 back to k.
# Maximum window size in this whole process is answer.

# Time: O(n), Space: O(1)
def longestOnes(nums: list[int], k: int) -> int:
    max_length = l = 0

    for r in range(len(nums)):
        # Reduce k by 1 for each zero seen. It's one less zero we can flip to 1.
        if nums[r] == 0:
            k -= 1

        # While window has over max amount of zeros (k < 0), shrink window from left
        while k < 0:
            # If old left window element was zero, add 1 back to k
            if nums[l] == 0:
                k += 1
            l += 1

        max_length = max(max_length, r - l + 1)

    return max_length

if __name__ == "__main__":
    assert longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2) == 6
    assert longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3) == 10
    assert longestOnes([0,0,0,0], 0) == 0
    print("All tests passed!")
