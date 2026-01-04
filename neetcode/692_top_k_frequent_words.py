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


# Min heap gets best Big O time!
# Time: O(n log k), Space: O(n)
def topKFrequentHeap(words: list[str], k: int) -> list[str]:
    """
    Simplest heap approach: Use nsmallest with correct key.
    """
    freq = Counter(words)
    sorted_freq = heapq.nsmallest(k, freq.items(), key=lambda x: (-x[1], x[0]))
    return [word for word, count in sorted_freq]


# Breakdown of heapq.nsmallest(k, freq.items(), key=lambda x: (-x[1], x[0])):

# 1. freq.items() → [('i', 2), ('love', 2), ('leetcode', 1), ('coding', 1)]
# Iterable of (word, count) tuples

# 2. key=lambda x: (-x[1], x[0])
# x = each (word, count) tuple
# x[0] = word, x[1] = count
# Transforms to (-count, word) for comparison only

# 3. Key transformation (for comparison):
# ('i', 2) → key = (-2, 'i')
# ('love', 2) → key = (-2, 'love')
# ('leetcode', 1) → key = (-1, 'leetcode')
# ('coding', 1) → key = (-1, 'coding')

# 4. nsmallest(k=2, ...) finds 2 smallest by key:
# Compares keys: (-2, 'i'), (-2, 'love'), (-1, 'leetcode'), (-1, 'coding')
# Smallest 2: (-2, 'i') and (-2, 'love')

# 5. Returns original items (not keys!):
# Returns: [('i', 2), ('love', 2)]
# Already sorted by the key function

# 6. Extract words:
# [word for word, count in sorted_freq] → ['i', 'love']
# Result: The k most frequent words, sorted by frequency (descending) then word (ascending).

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
