# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
# https://neetcode.io/solutions/kth-largest-element-in-an-array
# Min Heap: Fixed Size

import heapq

# Time: O(n log k), Space: O(k)
def findKthLargest(nums: list[int], k: int) -> int:
    heap = []

    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


if __name__ == "__main__":
    assert findKthLargest([3,2,1,5,6,4], 2) == 5
    assert findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4
    assert findKthLargest([2,3,1,5,4], 2) == 4
    assert findKthLargest([2,3,1,1,5,5,4], 3) == 4
    print("All tests passed!")
