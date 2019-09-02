# Problem: Implement a function to increment an arbitrary precision integer represented in the form of an array, where each element in the array corresponds to a digit.
#
# Examples:
# Input: [1,2,3]
# Output: [1,2,4]
#
# Explanation: 123 + 1 = 124
#
# Input: [5,8,9]
# Output: [5,9,0]
#
# Explanation: 589 + 1 = 590
def bigIntegerIncrement(arr):
    arrLen = len(arr)
    allNines = true
    for i in arr:
        if i != 9:
            allNines = false
            break

    result = [None]*(arrLen + 1) if allNines else [None]*arrLen

    sum = arr[arrLen - 1] + 1
    carry = sum / 10
    result[len(result) - 1] = sum % 10

    ptr1 = arrLen - 2
    ptr2 = len(result) - 2

    while ptr1 >= 0:
        sum = arr[ptr1] + carry
        carry = sum / 10
        result[ptr2] = sum % 10
        ptr1 -= 1
        ptr2 -= 1

    if allNines:
        result[0] = 1

    return result
