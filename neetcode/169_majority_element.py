# https://leetcode.com/problems/majority-element/description/?envType=company&envId=netflix&favoriteSlug=netflix-all
# https://neetcode.io/problems/majority-element/question?list=neetcode250

# Time: O(n), Space: O(n)
def majorityElement(nums: list[int]) -> int:
    freq = {}
    maxCount = len(nums) // 2

    for n in nums:
        freq[n] = freq.get(n, 0) + 1
        if freq[n] > maxCount:
            return n


# Even better! Boyer-Moore Voting Algorithm
# Time: O(n), Space: O(1)
# Video: https://www.youtube.com/watch?v=7pnhv842keE

# Since we have more majority elements than non-majority elements,
# cancel each possible majority element with a different element.
# The final element left uncancelled is the majority!
# "count" is not frequency of candidate. It's the candidate's lead after cancellations.

# def majorityElement(nums: list[int]) -> int:
#     candidate = count = 0

#     for n in nums:
#         if count == 0:
#             candidate = n

#         if n == candidate:
#             count += 1
#         else:
#             count -= 1

#     return candidate


if __name__ == "__main__":
    assert majorityElement([3, 2, 3]) == 3
    assert majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
    assert majorityElement([5]) == 5
    print("All tests passed!")

# Example of Boyer-Moore Voting Algorithm:

# nums = [2, 2, 1, 1, 1, 2, 2]

# | n | What happens            | candidate | count
# | 2 | no candidate → choose 2 |      2    |   1
# | 2 | same → +1               |      2    |   2
# | 1 | different → -1          |      2    |   1
# | 1 | different → -1          |      2    |   0
# | 1 | count=0 → choose 1      |      1    |   1
# | 2 | different → -1          |      1    |   0
# | 2 | count=0 → choose 2      | 2 (answer)|   1
