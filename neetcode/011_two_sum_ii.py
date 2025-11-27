# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?envType=problem-list-v2&envId=plakya4j
# https://neetcode.io/problems/two-integer-sum-ii/solution
# Like twoSum, but integer array is SORTED. "1-indexed" array: first index is 1, not 0.
# Use 2 pointers for indices, left and right.

# Time: O(n), Space: O(1)
def twoSum(numbers: list[int], target: int) -> list[int]:
    l, r = 0, len(numbers) - 1
    while l < r:
        sum = numbers[l] + numbers[r]

        if sum < target:
            l += 1
        elif sum > target:
            r -= 1
        else:
            return [l + 1, r + 1]


if __name__ == "__main__":
    assert twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert twoSum([2, 3, 4], 6) == [1, 3]
    assert twoSum([3, 3], 6) == [1, 2]
    assert twoSum([-1, 0], -1) == [1, 2]
    assert twoSum([2, 3, 3, 4], 6) == [1, 4]
    print("All tests passed!")
