# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
# https://neetcode.io/solutions/find-first-and-last-position-of-element-in-sorted-array
# Binary Search: Lower Bound (Twice)

# Time: O(log n), Space: O(1)
def searchRange(nums: list[int], target: int) -> list[int]:
    # LOWER BOUND(target)
    # First index whose value >= target
    l, r = 0, len(nums)

    while l < r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        else:             # nums[mid] >= target
            r = mid
    first = l

    # If target NOT in array. Either:
    # 1. We ran past end of array: first == len(nums)
    # 2. nums[first] != target
    if first == len(nums) or nums[first] != target:
        return [-1, -1]

    # UPPER BOUND(target) =  First index whose value > target = LOWER BOUND(target + 1) = l
    # But since we want last position of target, last = l - 1
    l, r = 0, len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid] < target + 1:
            l = mid + 1
        else:             # nums[mid] >= target + 1
            r = mid
    last = l - 1

    return [first, last]

if __name__ == "__main__":
    assert searchRange([5,7,7,8,8,10], 8) == [3,4]
    assert searchRange([5,7,7,8,8,10], 6) == [-1,-1]
    assert searchRange([], 0) == [-1,-1]
    assert searchRange([1], 1) == [0,0]
    print("All tests passed!")
