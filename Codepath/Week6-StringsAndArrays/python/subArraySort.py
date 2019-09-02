# Problem: Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.
#
# Example 1:
# Input: [1, 2, 5, 3, 7, 10, 9, 12]
# Output: 5
# Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted
# 
# Example 2:
# Input: [1, 3, 2, 0, -1, 7, 10]
# Output: 5
# Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted
def sort(arr):
    low = 0
    high = len(arr) - 1
    # find the first number out of sorting order from the beginning
    while low < len(arr) - 1 and arr[low] <= arr[low + 1]:
      low += 1

    if low == len(arr) - 1: # if the array is sorted
      return 0

    # find the first number out of sorting order from the end
    while high > 0 and arr[high] >= arr[high - 1]:
      high -= 1

    # find the maximum and minimum of the subarray
    subarrayMax = -float('inf')
    subarrayMin = float('inf')
    for k in range(low, high):
      subarrayMax = max(subarrayMax, arr[k])
      subarrayMin = min(subarrayMin, arr[k])

    # extend the subarray to include any number which is bigger than the minimum of the subarray
    while low > 0 and arr[low - 1] > subarrayMin:
      low -= 1
    # extend the subarray to include any number which is smaller than the maximum of the subarray
    while high < len(arr) - 1 and arr[high + 1] < subarrayMax:
      high += 1

    return high - low + 1
