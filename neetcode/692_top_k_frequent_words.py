# https://leetcode.com/problems/top-k-frequent-words/?envType=company&envId=netflix&favoriteSlug=netflix-all
# https://www.jointaro.com/interviews/questions/top-k-frequent-words/?company=netflix

from collections import Counter
import heapq


# Brute Force is simplest
# Time: O(n log n), Space: O(n)
def topKFrequent(words: list[str], k: int) -> list[str]:
    freq = Counter(words)

    # Sort by frequency (descending), then by word (ascending/lexicographical)
    # Use -count for descending order, word for ascending lexicographical order
    sorted_freq = sorted(freq.items(), key=lambda item: (-item[1], item[0]))

    # ...OR...
    # def sort_key(item):
    #     word, count = item
    #     return (-count, word)
    # sorted_words = sorted(freq.items(), key=sort_key)

    # Return first k words
    return [word for word, count in sorted_freq[:k]]


# Min heap is best Big O time, but hard to remember
# Time: O(n log k), Space: O(n)
def topKFrequentHeap(words: list[str], k: int) -> list[str]:
    """
    Min heap approach: More efficient when k << n.
    Manually maintain a min heap of size k using heappush/heappop.

    Key insight: We use (-count, word) as the heap key. When we need to remove
    an item (heap size > k), we want to remove the one with smallest count OR
    (same count AND largest word). This is the "largest" item by tuple comparison.
    Since heapq only gives us access to the smallest (root), we find and remove
    the worst item manually when needed.
    """
    freq = Counter(words)

    heap = []
    for word, count in freq.items():
        heapq.heappush(heap, (-count, word))
        if len(heap) > k:
            # Find the worst item to remove: smallest count or (same count, largest word)
            # In tuple terms: largest (-count, word) by comparison
            worst = max(heap)
            heap.remove(worst)
            heapq.heapify(heap)  # Re-heapify after removal

    # Sort final result: by -count (descending count), then word (ascending)
    result = sorted(heap)
    return [word for count, word in result]


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
