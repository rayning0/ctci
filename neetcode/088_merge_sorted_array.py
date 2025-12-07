# https://leetcode.com/problems/merge-sorted-array/description/
# https://neetcode.io/problems/merge-sorted-array/question?list=neetcode250
# Do not return anything! Must modify nums1 IN-PLACE! Use 3 pointers.
# This is very tricky, definitely a MEDIUM problem!

# Ex:   Pointers:   p1       p                   p2
# nums1 = [1, 2, 3, 4, 0, 0, 0]   nums2 = [3, 5, 6]
# p1 at end of nums1, length m
# p2 at end of nums2, length n
# p at end of nums1, length m + n

# Move p backwards in nums1 to create answer.

# Time: O(m + n), Space: O(1)
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    p1, p2 = m - 1, n - 1
    for p in range(m + n - 1, -1, -1):
        if p2 < 0:
            break
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1

    return nums1


if __name__ == "__main__":
    assert merge([1, 2, 3, 4, 0, 0, 0], 4, [3, 5, 6], 3) == [1, 2, 3, 3, 4, 5, 6]
    assert merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6]
    assert merge([1], 1, [], 0) == [1]
    assert merge([0], 0, [1], 1) == [1]
    assert merge([0, 0], 0, [1, 2], 2) == [1, 2]
    assert merge([10, 20, 20, 40, 0, 0], 4, [1, 2], 2) == [1, 2, 10, 20, 20, 40]
    print("All tests passed!")
