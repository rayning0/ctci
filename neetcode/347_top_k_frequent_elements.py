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
    buckets = [] # Never say buckets = ans = []!
    ans = []

    for n in nums:
        freq[n] = freq.get(n, 0) + 1

    # buckets is list of lists by frequency:
    # buckets[4] = [1, 2] = all nums with freq of 4
    # buckets has length len(nums) + 1, since nums could be all 1 number with frequency len(nums)
    for _ in range(len(nums) + 1):
        buckets.append([])
    # creates: [[], [], [], [], [], ...]

    # buckets = [[] for _ in range(len(nums) + 1)] means same thing, but hard to remember
    # buckets = [[]] * (len(nums) + 1) <--- WRONG!!!

    for n, count in freq.items():
        buckets[count].append(n)

    # from highest to lowest number count
    for count in range(len(nums), 0, -1):
        for n in buckets[count]:
            ans.append(n)
            if len(ans) == k:
                return ans

    # for vals in reversed(buckets):
    #     ans += vals  # concatenates lists
    #     if len(ans) >= k:
    #         # returns first k elements
    #         return ans[:k]


# Tests
if __name__ == "__main__":
    assert topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    # freq = {1: 3, 2: 2, 3: 1}
    # buckets = [[], [3], [2], [1], [], [], []]

    assert topKFrequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2) == [1, 2]
    # freq = {1: 4, 2: 4, 3: 2}
    # buckets = [[], [], [3], [], [1, 2], [], [], [], [], [], []]

    assert topKFrequent([1], 1) == [1]
    assert topKFrequent([7, 7], 1) == [7]

    print("All tests passed!")

# reversed():
# Built-in function for any iterable object: lists, tuples, strings, range, etc.
# Non-destructive: reversed() doesn't change original iterable. Instead, returns a reversed iterator object.
# Returns an iterator that yields the elements of the original iterable in reverse order. To get a new list or tuple, you need to explicitly convert iterator (e.g., using list() or tuple()).

# Use list.reverse() when you must reverse a list and no longer need the original order, and you want to save memory by modifying the list directly.

# Use reversed() when you must iterate over an iterable in reverse order without changing original, or when working with non-list iterables like strings or tuples.
