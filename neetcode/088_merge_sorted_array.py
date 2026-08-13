# https://leetcode.com/problems/merge-sorted-array/description/
# https://neetcode.io/problems/merge-sorted-array/question?list=neetcode250
# Must modify nums1 IN-PLACE! Use 2 pointers.
# This is really a MEDIUM problem!

# Ex:   Pointers:   p1       i                   p2
# nums1 = [1, 2, 3, 4, 0, 0, 0]   nums2 = [3, 5, 6]
# start p1 at end of nums1 (exclude 0's), length m
# start p2 at end of nums2, length n
# start i at end of nums1, length m + n

# Time: O(m + n), Space: O(1)
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    p1, p2 = m - 1, n - 1

    # loop backwards on nums1
    for i in range(m + n - 1, -1, -1):
        # If nums2 is exhausted, the remaining nums1 values are correctly positioned, so stop.
        if p2 < 0:
            break

        # If nums1 is exhausted, copy remaining nums2 values into num1.
        if p1 < 0 or nums1[p1] < nums2[p2]:
            nums1[i] = nums2[p2]
            p2 -= 1
        else:
            nums1[i] = nums1[p1]
            p1 -= 1

if __name__ == "__main__":
    nums1 = [1, 2, 3, 4, 0, 0, 0]
    merge(nums1, 4, [3, 5, 6], 3)
    assert nums1 == [1, 2, 3, 3, 4, 5, 6]

    nums1 = [1, 2, 3, 0, 0, 0]
    merge(nums1, 3, [2, 5, 6], 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    nums1 = [1]
    merge(nums1, 1, [], 0)
    assert nums1 == [1]

    nums1 = [0]
    merge(nums1, 0, [1], 1)
    assert nums1 == [1]

    nums1 = [0, 0]
    merge(nums1, 0, [1, 2], 2)
    assert nums1 == [1, 2]

    nums1 = [10, 20, 20, 40, 0, 0]
    merge(nums1, 4, [1, 2], 2)
    assert nums1 == [1, 2, 10, 20, 20, 40]

    nums1 = [-5, -2, 0, 0, 0]
    merge(nums1, 2, [-6, -3, 4], 3)
    assert nums1 == [-6, -5, -3, -2, 4]

    nums1 = [1, 1, 1, 0, 0]
    merge(nums1, 3, [1, 1], 2)
    assert nums1 == [1, 1, 1, 1, 1]

    print("All tests passed!")

# Ex:
# nums1 = [1, 2, 3, 4, 0, 0, 0], m = 4
# nums2 = [3, 5, 6], n = 3

# p1, p2 = m - 1 = 3, n - 1 = 2
# i = 6
# since nums1[3] < nums2[2] or nums1[p1] < nums2[p2]
# nums1[6] = nums2[2]       or nums1[i] = nums2[p2]

# nums1 = [1, 2, 3, 4, 0, 0, 6]
# nums2 = [3, 5, 6]
# p2 -= 1 = 1

# i = 5
# since nums1[3] < nums2[1] or nums1[p1] < nums2[p2]
# nums1[5] = nums2[1]       or nums1[i] = nums2[p2]

# nums1 = [1, 2, 3, 4, 0, 5, 6]
# nums2 = [3, 5, 6]
# p2 -= 1 = 0

# i = 4
# since nums1[3] >= nums2[0] or nums1[p1] >= nums2[p2]
# nums1[4] = nums1[3]        or nums1[i] = nums1[p1]

# nums1 = [1, 2, 3, 4, 4, 5, 6]
# nums2 = [3, 5, 6]
# p1 -= 1 = 2

# i = 3
# since nums1[2] == nums2[0] or nums1[p1] >= nums2[p2]
# nums1[3] = nums1[2]        or nums1[i] = nums1[p1]

# nums1 = [1, 2, 3, 3, 4, 5, 6]
# nums2 = [3, 5, 6]
# p1 -= 1 = 1

# i = 2
# since nums1[1] < nums2[0]  or nums1[p1] < nums2[p2]
# nums1[2] = nums2[0]        or nums1[i] = nums2[p2]

# nums1 = [1, 2, 3, 3, 4, 5, 6]
# nums2 = [3, 5, 6]
# p2 -= 1 = -1

# since p2 < 0 (done with nums2), return nums1
# __________
# Ex:
# nums1 = [0, 0], m = 0
# nums2 = [1, 2], n = 2

# p1, p2 = -1, 1
# i = 1

# since p1 < 0, <--- from the start, we can't use nums1 values
# nums1[1] = nums2[1] or nums1[p1] = nums2[p2]

# nums1 = [0, 2]
# p2 -= 1 = 0

# i = 0
# since p1 < 0,
# nums1[0] = nums2[0] or nums1[p1] = nums2[p2]

# nums1 = [1, 2] <---- basically, we copied all nums2 into nums1!
