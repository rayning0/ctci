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

# 1. Binary Search (2 sorted arrays)
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

# 2. Sweep Line (event list)
# def fullBloomFlowers(flowers: list[list[int]], people: list[int]) -> list[int]:

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
