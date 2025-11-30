# https://leetcode.com/problems/3sum/?envType=problem-list-v2&envId=plakya4j
# https://neetcode.io/problems/three-integer-sum/question?list=neetcode150

# Plan: Sort nums. Fix first element in outer loop.
# Then run 2nd loop, two-sum on remaining nums. See
# https://github.com/rayning0/ctci/blob/master/neetcode/011_two_sum_ii.py for Two-Sum on sorted list (uses pointers)
# Since nums is sorted, use 2 pointers to run 2-sum. Each time you find triplet, move outer pointer in.
# Plus, to avoid duplicate answers, must set 2 conditions!

# Time: O(n^2), Space: O(n)
def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []
    for i, n in enumerate(nums):
        # if new outer loop num is same outer loop num as before, skip to next outer loop num
        if i > 0 and n == nums[i - 1]:
            continue

        l = i + 1
        r = len(nums) - 1

        while l < r:
            sum = n + nums[l] + nums[r]
            if sum > 0:
                r -= 1
            elif sum < 0:
                l += 1
            else:
                res.append([n, nums[l], nums[r]])

                # move left pointer forward
                l += 1
                # but if its num == previous num for left pointer, keep moving it forward
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
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
