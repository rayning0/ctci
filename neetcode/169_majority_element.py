# https://leetcode.com/problems/majority-element/description/?envType=company&envId=netflix&favoriteSlug=netflix-all
# https://neetcode.io/problems/majority-element/question?list=neetcode250

from collections import Counter


# Time: O(n), Space: O(n)
def majorityElement(nums: list[int]) -> int:
    maxCount = len(nums) // 2
    freq = Counter(nums)

    # freq = {}
    # for n in nums:
    #     freq[n] = freq.get(n, 0) + 1

    for n, count in freq.items():
        if count > maxCount:
            return n


# Even better! Boyer-Moore Voting Algorithm
# Time: O(n), Space: O(1)
# Video: https://www.youtube.com/watch?v=7pnhv842keE
# def majorityElement(nums: list[int]) -> int:
#     res = count = 0
#     for num in nums:
#         if count == 0:
#             res = num

#         if num == res:
#             count += 1
#         else:
#             count -= 1

#         # count += (1 if num == res else -1) <-- compact way
#     return res


if __name__ == "__main__":
    assert majorityElement([3, 2, 3]) == 3
    assert majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
    assert majorityElement([5]) == 5
    print("All tests passed!")
