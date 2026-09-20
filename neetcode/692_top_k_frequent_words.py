# https://leetcode.com/problems/top-k-frequent-words/?envType=company&envId=netflix&favoriteSlug=netflix-all
# https://www.jointaro.com/interviews/questions/top-k-frequent-words/?company=netflix
# Max Heap
from collections import Counter
import heapq

# Brute Force
# Time: O(n log n), Space: O(n)
# def topKFrequent(words: list[str], k: int) -> list[str]:
#     freq = Counter(words)

#     # Sort by frequency (descending), then by word (ascending/lexicographical)
#     # Use -count for descending order, word for ascending lexicographical order
#     sorted_freq = sorted(freq.items(), key=lambda item: (-item[1], item[0]))

#     # ...OR...
#     #     word, count = item
#     #     return (-count, word)
#     # sorted_words = sorted(freq.items(), key=sort_key)

#     # Return first k words
#     return [word for word, count in sorted_freq[:k]]


# Max heap gets better Big O time!
# Because this pushes every unique word on heap, its Big-O time is
# Time: O(n + m log m + k log m) → O(n + m log m)
# Space: O(n)
# n = len(words). n >= m.
# m = # of unique words
# k = desired result size
def topKFrequent(words: list[str], k: int) -> list[str]:
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1            # O(n)

    max_heap = []
    ans = []

    for w, count in freq.items():
        heapq.heappush(max_heap, (-count, w))  # O(m log m)

    for _ in range(k):
        count, w = heapq.heappop(max_heap)     # O(k log m)
        ans.append(w)

    return ans

# Max Heap example:
# words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]

# 1. word freq:
#    {'the': 4, 'day': 1, 'is': 3, 'sunny': 2}

# 2. Push each word to heap as (-count, word).
#    "-count": makes higher frequency words pop out first.
#    Frequency 4 becomes -4. Since -4 is smaller, it pops out first.
#    Technically it's a min heap, but it simulates a max heap by frequency.

#    "word": For equal counts, Python sorts words alphabetically.

# 3. max_heap:
#    [(-4, 'the'), (-2, 'sunny'), (-3, 'is'), (-1, 'day')]

# 4. heapq.heappop(heap) removes smallest tuple + rearranges heap:
#    (-4, 'the') -> append 'the' to ans
# max_heap = [(-3, 'is'), (-2, 'sunny'), (-1, 'day')]
#    (-3, 'is') -> append 'is' to ans
# max_heap = [(-2, 'sunny'), (-1, 'day')]
#    (-2, 'sunny') -> append 'sunny' to ans

# 5. After k times, it returns words:
#    ["the", "is", "sunny", "day"]

Why is max heap better than min heap solution?

A. Max Heap:

Store (-frequency, word)

Python compares tuples left-to-right:
1. Higher frequency first (smaller negative frequency)
2. If tied, alphabetically smaller word first

Exactly matches problem requirements. No custom comparator needed.

B. Min Heap

(count, word) orders ties by alphabetically smaller words first.

But when the heap exceeds size k, we want to discard the "worst" word, which has:
- lowest frequency
- if freq is tied, alphabetically largest word

Python's default tuple ordering does the opposite, so we need a custom comparator (or wrapper class) Pair:

# Min Heap solution:

class Pair:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, p):
        return self.freq < p.freq or (self.freq == p.freq and self.word > p.word)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        h = []
        for word, freq in cnt.items():
            heappush(h, Pair(word, freq))
            if len(h) > k:
                heappop(h)
        return [p.word for p in sorted(h, reverse=True)]

if __name__ == "__main__":
    assert topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2) == ["i", "love"]
    assert topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4) == ["the", "is", "sunny", "day"]
    print("All tests passed!")
