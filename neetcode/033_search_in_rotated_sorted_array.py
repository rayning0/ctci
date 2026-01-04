# https://leetcode.com/problems/search-in-rotated-sorted-array/
# https://neetcode.io/solutions/search-in-rotated-sorted-array (Binary Search)

# Ex: [4,5,6,7,0,1,2] # nums[mid] > nums[-1]. pivot = 4. It's really
# [0,1,2,4,5,6,7] rotated left by pivot - 1 = 3


def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    # Find index of pivot (smallest element). pivot is where nums suddenly drop.
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] > nums[-1]:
            l = mid + 1  # pivot is to right
        else:
            r = mid - 1
    pivot = l

    # inner function
    def bsearch(l, r, target):
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1

    # Do binary search over 2 halves:
    # 1. Left of pivot
    index = bsearch(0, pivot - 1, target)
    if index != -1:
        return index

    # 2. From pivot to right
    return bsearch(pivot, len(nums) - 1, target)


if __name__ == "__main__":
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search([1], 0) == -1
    print("All tests passed!")
