# https://leetcode.com/problems/top-k-frequent-elements/description/?envType=problem-list-v2&envId=plakya4j
# https://neetcode.io/solutions/top-k-frequent-elements

# 1. Naive answer: Make freq hash of nums. Make array of [count, num].
# Sort it by count. Take last k elements.
# Time: O(n log n), Space: O(n + k)
# def topKFrequent(nums: list[int], k: int) -> list[int]:
#     freq = {}
#     for n in nums:
#         freq[n] = freq.get(n, 0) + 1

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
# Time: O(n log k), Space: O(n + k)
# import heapq

# def topKFrequent(nums: list[int], k: int) -> list[int]:
#     freq = {}
#     minHeap = []
#     for n in nums:
#         freq[n] = freq.get(n, 0) + 1

#     for n, count in freq.items():
#         heapq.heappush(minHeap, [count, n])
#         if len(minHeap) > k:
#             heapq.heappop(minHeap)  # delete all lower freq nums from heap
#     return [n for count, n in minHeap]
# OR  return [item[1] for item in minHeap]


# 3. Best! Bucket Sort
# Time: O(n), Space: O(n)
def topKFrequent(nums: list[int], k: int) -> list[int]:
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1

    # Make list of counts: index = count, value = [nums with that count]
    # Use list comprehension to create separate lists (not shared references!)
    # bucket = [[]] * (len(nums) + 1) <--- WRONG!!!
    bucket = [[] for i in range(len(nums) + 1)]
    # add 1 to size so we count freq from 1 to len(nums)

    for num, count in freq.items():
        bucket[count].append(num)

    res = []
    # Loop backwards, from highest to lowest count
    for vals in reversed(bucket):
        res += vals  # concatenates lists
        if len(res) >= k:
            # returns first k elements
            return res[:k]


# for i in range(len(bucket) - 1, -1, -1):
#     for num in bucket[i]:
#         res.append(num)
#         if (len(res)) == k:
#             return res


# Tests
if __name__ == "__main__":
    assert topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    # freq = {1: 3, 2: 2, 3: 1}
    # bucket = [[], [3], [2], [1], [], [], []]

    assert topKFrequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2) == [1, 2]
    # freq = {1: 4, 2: 4, 3: 2}
    # bucket = [[], [], [3], [], [1, 2], [], [], [], [], [], []]

    assert topKFrequent([1], 1) == [1]
    assert topKFrequent([7, 7], 1) == [7]

    print("All tests passed!")

# WRONG!
# for n in nums.reverse():
#     print(n)

# nums.reverse() returns None. Can't loop over it!

# RIGHT:
# for n in reversed(nums):
#     print(n)

# reversed() and reverse() are used to reverse the order of elements, but differ in their application, return value, and whether they modify the original object.

# 1. list.reverse() Method:
# Applicability: Only for Python lists. Can't with with other iterables like strings or tuples.
# Changes list in-place. Directly changes the order of elements in original list object.
# Returns None. It does not create new list or return reversed version; it simply changes existing list.

# 2. reversed():
# Built-in function for any iterable object: lists, tuples, strings, range, etc.
# Non-destructive: reversed() doesn't change original iterable. Instead, returns a reversed iterator object.
# Returns an iterator that yields the elements of the original iterable in reverse order. To get a new list or tuple, you need to explicitly convert iterator (e.g., using list() or tuple()).

# Use list.reverse() when you must reverse a list and no longer need the original order, and you want to save memory by modifying the list directly.

# Use reversed() when you must iterate over an iterable in reverse order without changing original, or when working with non-list iterables like strings or tuples.
