# https://leetcode.com/problems/product-of-array-except-self/?envType=problem-list-v2&envId=plakya4j
# https://neetcode.io/solutions/product-of-array-except-self

#           0      1          2           3        = i
#          [4,     5,         10,         15  ]    = nums
#     [     1      1*4        1*4*5     1*4*5*10 ] = left product (prefix)
#     [ 1*5*10*15  1*10*15    1*15         1     ] = right product (suffix)
# __________________________________________________
# Multiply down vertically:
#      [1*5*10*15  1*4*10*15  1*4*5*15  1*4*5*10 ] = Answer

# def productExceptSelf(nums: list[int]) -> list[int]:
#     size = len(nums)
#     left, right = [1] * size, [1] * size

#     for i in range(1, size):  # left index from 1 to size - 1
#         left[i] = left[i - 1] * nums[i - 1]

#     for j in range(size - 2, -1, -1):  # right index from size - 2 (1 before end) to 0
#         right[j] = right[j + 1] * nums[j + 1]

#     # list comprehension
#     return [left[i] * right[i] for i in range(size)]
#     # return [l * r for l, r in zip(left, right)] <--- could use zip()

# Time: O(n), Space: O(n) for output prefix/suffix lists, O(1) for extra space
def productExceptSelf(nums: list[int]) -> list[int]:
    size = len(nums)
    left = right = 1
    prefix, suffix = [1] * size, [1] * size

    for i in range(1, size):
        left *= nums[i - 1]
        prefix[i] = left

    for i in range(size - 2, -1, -1):
        right *= nums[i + 1]
        suffix[i] = right

    # print (f"prefix: {prefix}")
    # print (f"suffix: {suffix}")

    return [prefix[i] * suffix[i] for i in range(size)]


if __name__ == "__main__":
    assert productExceptSelf([4, 5, 10, 15]) == [750, 600, 300, 200]
    assert productExceptSelf([5, 6, 2, 10]) == [120, 100, 300, 60]
    assert productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    print("All tests passed!")
