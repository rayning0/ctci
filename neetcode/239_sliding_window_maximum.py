# https://leetcode.com/problems/sliding-window-maximum/description/
# https://neetcode.io/solutions/sliding-window-maximum
# Monotonic Deque: Sliding Window

# 1. Monotonic Deque: Sliding Window. BEST for interviews!
# Deque stores (value, index) for max candidates only. It does NOT store all values in sliding window.
# When new max candidate arrives, we delete all smaller candidates in deque.
# Values are always in decreasing order. ("Monotonic decreasing queue")
# Front = q[0] = max candidate in current window = (max_val, index of max_val) = (q[0][0], q[0][1])
# Back = q[-1] = smallest candidate remaining in queue
# q[-1][0] = last val in queue

# Delete expired values (outside window) from the front.
# Delete smaller values (than curr_val) from the back.

# Time: O(n), Space: O(k)
from collections import deque
def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    max = []
    q = deque()
    l = r = 0

    while r < len(nums):
        curr_val = nums[r]
        # Delete all smaller vals (< current val) from back of queue.
        # They can never become the max val while curr_val remains in the window, since curr_val is newer and larger.
        # Keep popping queue (from right) till current val is not > last val in queue (q[-1][0]).
        while q and curr_val > q[-1][0]:
            q.pop()
        # Ex: q = [(9,_), (7,_), (6,_)]. curr_val = 8. while loop deletes [(7,_), (6,_)] since they're < 8.
        # After q.append(), resulting q = [(9,_), (8,_)]

        # Adds only monotonically DECREASING vals to queue. Thus:
        # q[0] maximum candidate (thus it's max val of current window)
        # q[-1] smallest candidate still left in queue
        q.append((curr_val, r))

        # Delete all expired vals from front of queue.
        # If max val in current window has expired (i.e. its index (q[0][1]) < l), delete it (from left)
        if q[0][1] < l:
            q.popleft()

        # Ex: k = 3. nums = [1,3,-1,-3,5,3,6,7]
        # At r = 2 = k - 1, we hit end of first sliding window (size 3).
        # If r >= end of first sliding window, add max_val to max.
        if r >= k - 1:
            max.append(q[0][0])    # q[0][0] = max_val in current window
            l += 1
        r += 1

    return max

# 2. Max Heap: Heap + index + lazy deletion

# Don't remove expired elements from heap immediately. Give every heap element its index,
# and delete expired elements only when they reach top of max heap, called "lazy deletion."
# Some elements still in heap may be outside window, but if not at top, ignore them.

# Heap is NOT the sliding window. It's a leaderboard of possible max values.
# Old possible max values stay on leaderboard till they rise to top. Only then do we discover they're expired and remove them.

# Time: O(n log n), Space: O(n)
import heapq
def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    heap, max = [], []

    for i in range(len(nums)):
        heapq.heappush(heap, (-nums[i], i))
        l = i - k + 1   # left side of window
        if l >= 0:
            # Lazy deletion:
            # Delete expired elements (outside window) only if they become the heap maximum.
            # Expired elements deeper in heap can't affect the answer, so ignore them.
            # heap[0][1] = index of max value in heap
            while heap[0][1] < l:
                heapq.heappop(heap)

            # -heap[0][0] = max value in heap
            max.append(-heap[0][0])

    return max

if __name__ == "__main__":
    assert maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
    assert maxSlidingWindow([1,2,1,0,4,2,6], 3) == [2,2,4,4,6]
    assert maxSlidingWindow([1,3,1,2,0,5], 3) == [3,3,2,5]
    assert maxSlidingWindow([1], 1) == [1]
    print("All tests passed!")
________________
Example with deque:

nums = [1,3,1,2,0,5], k = 3

r=0, val=1
Deque: [(1,0)]

r=1, val=3
3 > 1 → pop (1,0)
Deque: [(3,1)]

r=2, val=1
Append (1,2)
Deque: [(3,1),(1,2)]
Window [1,3,1] → max = 3

r=3, val=2
2 > 1 → pop (1,2)
Append (2,3)
Deque: [(3,1),(2,3)]
Window [3,1,2] → max = 3

r=4, val=0
Append (0,4)
Deque: [(3,1),(2,3),(0,4)]
Index 1 expired → pop left
Deque: [(2,3),(0,4)]
Window [1,2,0] → max = 2

r=5, val=5
5 > 0 → pop
5 > 2 → pop
Append (5,5)
Deque: [(5,5)]
Window [2,0,5] → max = 5

Answer: [3,3,2,5]
