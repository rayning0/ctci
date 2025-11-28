# https://leetcode.com/problems/top-k-frequent-elements/
# https://neetcode.io/solutions/top-k-frequent-elements

from collections import Counter


# 1. Naive answer: Make freq hash of nums. Make array of [count, num].
# Sort it by count. Take last k elements.
# Time: O(n log n), Space: O(n)
# def topKFrequent(nums: list[int], k: int) -> list[int]:

#     freq = Counter(nums)
#       ...OR...
#     freq = {}
#     # for n in nums:
#     #     freq[n] = freq.get(n, 0) + 1

#     arr = []
#     for num, count in freq.items():
#         arr.append([count, num])
#     arr.sort()

#     res = []
#     while len(res) < k:
#         res.append(arr.pop()[1])
#     return res

# 2. Better: MinHeap with size limit
# Delete all lower freq nums from heap. Only max freq nums remain.
# Time: O(n log k), Space: O(n)
# import heapq


# def topKFrequent(nums: list[int], k: int) -> list[int]:
#     minHeap = []
#     freq = Counter(nums)

#     for num, count in freq.items():
#         heapq.heappush(minHeap, [count, num])
#         if len(minHeap) > k:
#             heapq.heappop(minHeap)  # delete all lower freq nums from heap

#     return [item[1] for item in minHeap]
# OR return [num for count, num in minHeap]


# 3. Best! Bucket Sort
# Time: O(n), Space: O(n)
def topKFrequent(nums: list[int], k: int) -> list[int]:
    freq = Counter(nums)
    #     OR
    # freq = {}
    # for n in nums:
    #   freq[n] = freq.get(n, 0) + 1
    #     OR
    # freq = {}
    # for n in nums:
    #   if n in freq:
    #       freq[n] += 1
    #   else:
    #       freq[n] = 0

    # Make list of counts: index = count, value = [nums with that count]
    bucket = [[] for i in range(len(nums) + 1)]
    # add 1 to size so we count freq from 1 to len(nums)

    for num, count in freq.items():
        bucket[count].append(num)

    res = []
    # Loop backwards through counts (highest to lowest count)
    for vals in reversed(bucket):
        res += vals  # concatenates lists
        if len(res) >= k:
            # returns first k elements
            return res[:k]

    # for i in range(len(bucket) - 1, 0, -1):
    #     for num in bucket[i]:
    #         res.append(num)
    #         if (len(res)) == k:
    #             return res


# Tests
if __name__ == "__main__":
    assert topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert topKFrequent([1], 1) == [1]
    assert topKFrequent([7, 7], 1) == [7]
    assert topKFrequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2) == [1, 2]
    print("All tests passed!")
