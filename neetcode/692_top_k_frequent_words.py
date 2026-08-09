# https://leetcode.com/problems/top-k-frequent-words/?envType=company&envId=netflix&favoriteSlug=netflix-all
# https://www.jointaro.com/interviews/questions/top-k-frequent-words/?company=netflix

from collections import Counter
import heapq


# Brute Force
# Time: O(n log n), Space: O(n)
def topKFrequent(words: list[str], k: int) -> list[str]:
    freq = Counter(words)

    # Sort by frequency (descending), then by word (ascending/lexicographical)
    # Use -count for descending order, word for ascending lexicographical order
    sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    # ...OR...
    # def sort_key(item):
    #     word, count = item
    #     return (-count, word)
    # sorted_words = sorted(freq.items(), key=sort_key)

    # Return first k words
    return [word for word, count in sorted_freq[:k]]


# Min heap gets better Big O time!
# Because this pushes every unique word on heap, its Big-O time is
# Time: O(n + m log m + k log m) → O(n + m log m). m = # of unique words
# Space: O(n)
def topKFrequentHeap(words: list[str], k: int) -> list[str]:
    """
    Simplest heap approach:
    """
    freq = Counter(words) # O(n)
    heap = []
    ans = []

    for word, count in freq.items():
        heapq.heappush(heap, (-count, word)) # O(m log m)

    for _ in range(k):
        count, word = heapq.heappop(heap) # O(k log m)
        ans.append(word)

    return ans


# Breakdown of heap approach:

# 1. Counter(words) creates word/count pairs:
#    {'i': 2, 'love': 2, 'leetcode': 1, 'coding': 1}

# 2. Push each word as (-count, word).
#    Negative count makes higher-frequency words come out first:
#    Frequency 2 becomes -2. Since -2 is smaller, it pops out first.
#    Technically it's a min heap, but it simulates like a max heap by frequency.

#    For equal counts, Python compares words alphabetically.


# 3. The heap contains:
#    (-2, 'i'), (-2, 'love'), (-1, 'leetcode'), (-1, 'coding')

# 4. heapq.heappop(heap) removes the smallest tuple:
#    (-2, 'i') -> append 'i'
#    (-2, 'love') -> append 'love'

# 5. Repeat k times and return the words:
#    ['i', 'love']



if __name__ == "__main__":
    # Test original function
    assert topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2) == [
        "i",
        "love",
    ]
    assert topKFrequent(
        ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4
    ) == ["the", "is", "sunny", "day"]
    print("Original function: All tests passed!")

    # Test heap function
    assert topKFrequentHeap(["i", "love", "leetcode", "i", "love", "coding"], 2) == [
        "i",
        "love",
    ]
    assert topKFrequentHeap(
        ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4
    ) == ["the", "is", "sunny", "day"]
    print("Heap function: All tests passed!")
