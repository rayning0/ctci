# https://leetcode.com/problems/kth-largest-element-in-a-stream/
# https://neetcode.io/solutions/kth-largest-element-in-a-stream
# Min Heap: Fixed Size

import heapq

# Time: O(m log k), Space: O(k)
# m = number of times add() called
class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = []  # min heap

        for n in nums:
            heapq.heappush(self.heap, n)    # O(log k)
            if len(self.heap) > k:
                heapq.heappop(self.heap)

    # Time: O(log k), Space: O(k)
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)  # O(log k)

        # pop all smaller elements than the top k.
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # smallest element in top k = kth largest element! just return number at top of min heap.
        return self.heap[0]


if __name__ == "__main__":
    obj = KthLargest(3, [4, 5, 8, 2])
    assert obj.add(3) == 4
    assert obj.add(5) == 5
    assert obj.add(10) == 5
    assert obj.add(9) == 8
    assert obj.add(4) == 8

    obj = KthLargest(4, [7, 7, 7, 7, 8, 3])
    assert obj.add(2) == 7
    assert obj.add(10) == 7
    assert obj.add(9) == 7
    assert obj.add(9) == 8

    obj = KthLargest(3, [1, 2, 3, 3])
    assert obj.add(3) == 3
    assert obj.add(5) == 3
    assert obj.add(6) == 3
    assert obj.add(7) == 5
    assert obj.add(8) == 6
    print("All tests passed!")
