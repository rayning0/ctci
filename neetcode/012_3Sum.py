# https://leetcode.com/problems/3sum/?envType=problem-list-v2&envId=plakya4j
# https://neetcode.io/problems/three-integer-sum/question?list=neetcode150

# Plan: Sort nums. Fix first index (i) in outer loop.
# Sorting nums lets us run 2nd loop, two-sum solution on remaining indices (j, k). See
# https://github.com/rayning0/ctci/blob/master/neetcode/011_two_sum_ii.py for Two-Sum on sorted list (uses pointers)
# Use 2 pointers to run 2-sum. Each time you find triplet, move outer pointer in.
# To avoid duplicate answers, set 3 duplicate conditions below!
# We can sort nums since sorting is O(n log n), but overall we have 2 nested loops O(n^2), so sorting time doesn't matter.

# Time: O(n^2), Space: O(n)
def threeSum(nums: list[int]) -> list[list[int]]:
    size = len(nums)
    nums.sort()  # sort nums to allow two-sum solution with j, k
    res = []

    for i in range(size):
        # Skip duplicate num #1: If num #1 repeats last num #1, i += 1
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = size - 1

        # Two-sum algorithm on num #2 and #3: Lines 25-33
        while j < k:
            sum = nums[i] + nums[j] + nums[k]

            if sum > 0:
                k -= 1
            elif sum < 0:
                j += 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1

                # Skip duplicate num #2: If num #2 repeats last num #2, j += 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1

                # Skip duplicate num #3: If num #3 repeats last num #3, k -= 1. We subtract since k moves left.
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1

    return res


if __name__ == "__main__":
    assert threeSum([-100, -70, -60, 110, 120, 130, 160]) == [
        [-100, -60, 160],
        [-70, -60, 130],
    ]
    assert threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert threeSum([0, 1, 1]) == []
    assert threeSum([0, 0, 0]) == [[0, 0, 0]]
    print("All tests passed!")
