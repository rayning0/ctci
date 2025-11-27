# https://leetcode.com/problems/two-sum/?envType=problem-list-v2&envId=plakya4j
# https://neetcode.io/problems/two-integer-sum/solution

# Time: O(n), Space: O(n)
def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        else:
            seen[num] = i


if __name__ == "__main__":
    assert twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert twoSum([3, 2, 4], 6) == [1, 2]
    assert twoSum([3, 3], 6) == [0, 1]
    print("All tests passed!")
