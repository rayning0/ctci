# https://leetcode.com/problems/contiguous-array/
# https://neetcode.io/solutions/contiguous-array

# Time: O(n), Space: O(n)
def findMaxLength(nums: list[int]) -> int:
    count = 0
    max_length = 0
    counts = {0: -1} # use -1 as start index to calculate subarray length

    for i, n in enumerate(nums):
        if n == 1:
            count += 1
        else:
            count -= 1

        if count in counts:
            length = i - counts[count]
            max_length = max(max_length, length)
        else:
            counts[count] = i

    return max_length


if __name__ == "__main__":
    assert findMaxLength([0,1]) == 2
    assert findMaxLength([0,1,0]) == 2
    assert findMaxLength([0,1,1,1,1,1,0,0,0]) == 6
    assert findMaxLength([1,0,0,1,1,1,1,0,0,0,1]) == 10
    print("All tests passed!")

# - Answer must be even
# - If n == 1, count += 1. If n == 0, count -= 1.
# - Make hashmap counts. key = count, val = index.
# - The longest subarray between 2 SAME count values is the answer!

# nums =      [0, 1,  1,  1,  1,  1,  0,  0,  0]
# count:    0 -1  0   1   2   3   4   3   2   1
# index:   -1  0  1   2   3   4   5   6   7   8

# counts = {
#      0: -1 <-- at index 1, saw count 0 before at index -1. max_length = 1 -(-1) = 2
#     -1:  0
#      1:  2 <-- at index 8, saw count 1 before at index 2. max_length = 8 - 2 = 6 <--- ANSWER!
#      2:  3 <-- at index 7, saw count 2 before at index 3. max_length = 7 - 3 = 4
#      3:  4 <-- at index 6, saw count 3 before at index 4. length = 6 - 4 = 2. not > max_length, so skip it.
#      4:  5
# }
# max_length = 6

# nums =      [1, 0,  0,  1,  1,  1,  1,  0,  0,  0,  1]
# count:    0  1  0  -1   0   1   2   3   2   1   0   1
# index:   -1  0  1   2   3   4   5   6   7   8   9  10

# counts = {
#    -1:  2
#     0: -1 <-- at index 1, saw count 0 before at index -1. max_length = 1 -(-1) = 2  subarray: [1,0]
#           <-- at index 3, saw count 0 before at index -1. max_length = 3 -(-1) = 4. subarray: [1,0,0,1]
#           <-- at index 9, saw count 0 before at index -1. max_length = 9 - 0 = 9. subarray: [1,0,0,1,1,1,1,0,0,0]
#     1:  0 <-- at index 4, saw count 1 before at index  0. length = 4 - 0 = 4. subarray: [0,0,1,1]
#           <-- at index 8, saw count 1 before at index  0. max_length = 8 - 0 = 8. subarray: [0,0,1,1,1,1,0,0]
#           <-- at index 10, saw count 1 before at index 0. max_length = 10-0 = 10. subarray: [0,0,1,1,1,1,0,0,0,1] <-- ANSWER!
#     2:  5 <-- at index 7, saw count 2 before at index  5. length = 7 - 5 = 2. subarray: [1,0]
#     3:  6
# }
# max_length = 10
