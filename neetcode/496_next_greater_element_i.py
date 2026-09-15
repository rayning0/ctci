# https://leetcode.com/problems/next-greater-element-i/description/
# https://neetcode.io/solutions/next-greater-element-i
# Monotonic Stack

# While looping through nums2, find next greater element for all num2 values seen so far.
# Precompute "next greater element" for all nums2 elements in 1 pass, store in map.
# Use monotonic stack while looping through nums2.
# Looping through nums1, look up answers in map for ans.

# Similar solution: https://github.com/rayning0/ctci/blob/master/neetcode/739_daily_temperatures.py

# 1. Monotonic Stack
# Time: O(n + m), Space: O(m)
# n = len(nums1), m = len(nums2)
# Each element is pushed/popped from stack at most once (amortized O(1)), so nums2 loop is O(m) space.
def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    stack, ans = [], []

    # key = num2, val = next greater num than num2
    next_greater = {}

    for num2 in nums2:
        # Keep popping stack till value is not greater than top value of stack
        while stack and num2 > stack[-1]:
            next_greater[stack.pop()] = num2

        # In stack, store each num2 that has NOT yet seen greater value.
        # It makes a "monotonic decreasing stack", since stack values drop until we hit a greater value.
        stack.append(num2)

    # For all nums left in stack, set vals to -1. We never found their next greater values.
    for num in stack:
        next_greater[num] = -1

    for num1 in nums1:
        ans.append(next_greater[num1])

    return ans

# 2. Brute Force:

# Time: O(n * m), Space: O(1) auxiliary
# n = len(nums1), m = len(nums2)
# def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
#     ans = [-1] * len(nums1)
#     for i, num1 in enumerate(nums1):
#         found = False
#         for j, num2 in enumerate(nums2):
#             if found and num2 > num1:
#                 ans[i] = num2
#                 break

#             if num2 == num1:
#                 found = True

#     return ans

if __name__ == "__main__":
    assert nextGreaterElement([4,1,2], [1,3,4,2]) == [-1,3,-1]
    assert nextGreaterElement([2,4], [1,2,3,4]) == [3,-1]
    print("All tests passed!")
