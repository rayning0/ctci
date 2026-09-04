# https://leetcode.com/problems/number-of-flowers-in-full-bloom/description/
# https://neetcode.io/solutions/number-of-flowers-in-full-bloom
# Intervals: Upper + Lower Bound Binary Search

# INSIGHT: Blooming flowers a person sees at time =
# flowers that started blooming - flowers that stopped blooming.
# Binary search list of sorted start times to count flowers that started blooming at time.
# Binary search list of sorted end times to count flowers that stopped blooming by time.

# For flower to bloom, start <= time <= end
# flowers started blooming = count(start <= time) = first value > time
# flowers stopped blooming = count(end < time) = first value >= time

# lower_bound(time) = first value >= time
#                   = count of values < time
#                   = bisect_left(end, time)

# upper_bound(time) = first value > time
#                   = count of values <= time
#                   = bisect_right(start, time)

# Remember, any index in list = # of items that come before it.

# EXAMPLE:
# start = [1, 3, 4, 9]
# end = [6, 7, 12, 13]

# If person looks at time 7,
# How many flowers already blooming?            start <= 7.
# [1, 3, 4 | 9] = 3 flowers
# count of values <= 7 | upper_bound(7) = first value > 7 | bisect_right(start, 7) all mean SAME!


# How many flowers already stopped blooming?    end < 7.
# [6 | 7, 12, 13] = 1 flower
# count of values < 7 | lower_bound(7) = first value >= 7 | bisect_left(end, 7) all mean SAME!

# So actual flowers blooming at time 7 = 3 - 1 = 2 flowers.

# 1. Binary Search (2 sorted arrays). BEST for interview!
from bisect import bisect_left, bisect_right

# Time: O((n + m) log n), Space: O(n) auxiliary
# n = len(flowers), m = len(people)
def fullBloomFlowers(flowers: list[list[int]], people: list[int]) -> list[int]:
    start, end, ans = [], [], []
    for s, e in flowers:
        start.append(s)
        end.append(e)
    start.sort()
    end.sort()

    for time in people:
        # flowers start blooming when start times <= time
        # upper_bound(time) = first value > time
        started = bisect_right(start, time)

        # l, r = 0, len(start)
        # while l < r:
        #     mid = (l + r) // 2
        #     if start[mid] > time:
        #         r = mid
        #     else:
        #         l = mid + 1

        # started = l

        # flowers stop blooming when end times < time
        # lower_bound(time) = first value >= time
        ended = bisect_left(end, time)

        # l, r = 0, len(end)
        # while l < r:
        #     mid = (l + r) // 2
        #     if end[mid] >= time:
        #         r = mid
        #     else:
        #         l = mid + 1

        # ended = l

        ans.append(started - ended)

    return ans

# 2. Sweep Line (event list). Hard to remember.
# See "Sweep Line with sorted event list" answer:
# https://github.com/rayning0/ctci/blob/e75c87f4433a7dce96371d4d244092828bf2e5e2/neetcode/1094_car_pooling.py#L33

# Sort flower events and people by time. Sweep through both once, processing every flower event before answering each person's query.

3 event types:
1. flower starts bloom:  +1 blooming flower   = (start time,   +1)
2. flower stops bloom:   -1 blooming flower   = (end time + 1, -1). Use "end time + 1" since flowers still bloom at end time.
3. person arrives to ask current bloom count  = (time, person index)

Example:
flowers = [[1,6], [3,7], [4,5]]
people = [2,5,7]

Events:
start = [(1, +1), (3, +1), (4, +1)]
end   = [(7, -1), (8, -1), (6, -1)]
asks  = [(2, 0), (5, 1), (7, 2)]

Sort all events by time:

Time    Event           Change      Blooming Flowers
1       flower starts   +1          1
2       person asks                 1   *
3       flower starts   +1          2
4       flower starts   +1          3
5       person asks                 3   *
6       flower ends     -1          2
7       flower ends     -1          1
7       person asks                 1   *
8       flower ends     -1          0

ans = [1, 3, 1]

# Time: O(n log n + m log m), Space: O(n + m) auxiliary
# n = len(flowers), m = len(people)
def fullBloomFlowers(flowers: list[list[int]], people: list[int]) -> list[int]:
    flower_events, asks = [], []
    ans = [0] * len(people)

    for start, end in flowers:
        flower_events.append((start, 1))       # for each start time, 1 new flower blooms
        flower_events.append((end + 1, -1))    # for each end + 1 time, 1 old flower stops blooming
    flower_events.sort()

    for i, time in enumerate(people):
        asks.append((time, i))

    asks.sort()

    blooming = j = 0
    for time, person_index in asks:

        # Loop through flower events for all times <= each person's ask time
        while j < len(flower_events) and flower_events[j][0] <= time:
            # add flower event's change value (+1 or -1)
            blooming += flower_events[j][1]
            j += 1

        ans[person_index] = blooming

    return ans

# 3. Brute Force
# Time: O(n * m). n = len(flowers), m = len(people)
# def fullBloomFlowers(flowers: list[list[int]], people: list[int]) -> list[int]:
#     ans = []

#     for time in people:
#         count = 0
#         for start, end in flowers:
#             if start <= time <= end:
#                 count += 1
#         ans.append(count)

#     return ans

#     *   *               *                *
# 1   2   3   4   5   6   7   8   9   10  11  12  13
# ---------------------
#         -----------------
#                                 --------------
#             --------------------------------------
#     |   |               |                |
#    [1   2               2                2]

if __name__ == "__main__":
    assert fullBloomFlowers([[1,6],[3,7],[9,12],[4,13]], [2,3,7,11]) == [1,2,2,2]
    assert fullBloomFlowers([[1,10],[3,3]], [3,3,2]) == [2,2,1]
    print("All tests passed!")
