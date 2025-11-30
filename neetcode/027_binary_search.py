# https://leetcode.com/problems/binary-search/?envType=problem-list-v2&envId=plakya4j
# https://neetcode.io/problems/binary-search/question?list=neetcode150

# Time: O(log n), Space: O(1)
def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            return mid
    return -1


if __name__ == "__main__":
    assert search([5], 5) == 0
    assert search([-1, 0, 3, 5, 9], 9) == 4  # tricky for odd size
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert search([-1, 0, 2, 4, 6, 8], 4) == 3
    assert search([-1, 0, 2, 4, 6, 8], 3) == -1
    print("All tests passed!")
