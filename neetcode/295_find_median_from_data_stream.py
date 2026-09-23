# https://leetcode.com/problems/find-median-from-data-stream/description/
# https://neetcode.io/solutions/find-median-from-data-stream
# 2 Heaps: Min Heap + Max Heap

# Divide input array in 2 parts:
# 1. Use min heap for greater half
# 2. Use max heap for lesser half
# 3. max_heap <= median <= min_heap
# 4. If total elements is odd, median is element from half with larger size.

# 1. Decide which half new input goes to
# 2. Insert it there
# 3. Rebalance if a heap size gets too big.

import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap = []  # for greater half of input
        self.max_heap = []  # for lesser half of input
        # self.max_heap <= median <= self.min_heap

    # Time: O(log n), Space: O(n)
    def addNum(self, num: int) -> None:
        # if num > bottom of greater half, push it in greater half
        if self.min_heap and num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush_max(self.max_heap, num)

        # Rebalance if a heap's length > len(other heap) + 1
        if len(self.min_heap) > len(self.max_heap) + 1:
            popmin = heapq.heappop(self.min_heap)
            heapq.heappush_max(self.max_heap, popmin)
        if len(self.max_heap) > len(self.min_heap) + 1:
            popmax = heapq.heappop_max(self.max_heap)
            heapq.heappush(self.min_heap, popmax)

    # Time: O(1), Space: O(1)
    def findMedian(self) -> float:
        # return top of longer half
        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0]
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        # Both halves same length. Return average.
        return (self.min_heap[0] + self.max_heap[0]) / 2

if __name__ == "__main__":
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    assert obj.findMedian() == 1.5
    obj.addNum(3)
    assert obj.findMedian() == 2.0

    obj = MedianFinder()
    obj.addNum(1)
    assert obj.findMedian() == 1.0
    obj.addNum(3)
    assert obj.findMedian() == 2.0
    obj.addNum(2)
    assert obj.findMedian() == 2.0
    print("All tests passed!")

# Followups:

# 1. If all integer numbers in range [0, 100], how to optimize solution?

# Use a counting array (bucket approach):

# Keep array count[101] where count[i] = frequency of i, plus a running total count.
# addNum: count[num] += 1, total += 1 → O(1)

# findMedian: Walk through count[], accumulating frequencies until you reach the total // 2-th element.
# This takes O(100) = O(1) time.

# This is better to heap approach, since both operations become constant time.
# ________________
# 2. If 99% of all integer numbers in the range [0, 100], how to optimize solution?

# Combine both approaches:

# - A count[101] array for numbers in [0, 100]
# - 2 small lists/heaps for outliers: one for < 0, one for > 100
# - Since only 1% are outliers, those lists stay tiny. When finding the median:

# We know total count in bucket array and in each outlier list.
# The median almost always falls inside [0, 100], so just scan the counting array.
# In rare case the median falls in the outlier range, sort/scan those small lists.

# Result: addNum is O(1) (just increment a counter or append to a tiny list).
# findMedian is O(100 + k), where k = number of outliers, effectively O(1).
