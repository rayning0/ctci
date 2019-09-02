# Problem: Given an input string, write a function that returns the run-length encoded string for the input string.
#
# Example:
# Input: "wwwwaaadexxxxxx"
# Output: "w4a3d1e1x6"
def compute(s):
    arr = list(s)
    result = []

    i = 0
    j = 1
    while i < len(arr):
        count = 1
        while j < len(arr) and arr[i] == arr[j]:
            j += 1
            count += 1

        if count > 1:
            result.append(count)
            result.append(arr[i])
        else:
            result.append(arr[i])

        if len(result) > len(s):
            break

        i = j
        j = i + 1

    return ''.join(arr)
