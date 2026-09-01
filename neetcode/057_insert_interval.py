# https://leetcode.com/problems/insert-interval/
# https://neetcode.io/solutions/insert-interval
# Intervals: Greedy Merge (Already Sorted)

# Intervals are already sorted and do NOT overlap.

# 1. Greedy. Best for interview! 1-pass solution.

# Scan intervals from left to right. newInterval is 1 of 3 cases compared to each interval.

# 1. newInterval ends before this interval:
# Then no later interval will overlap with it either.
# So append newInterval to ans, then immediately return ans + rest of intervals.

# 2. newInterval starts after this interval:
# Then append interval to ans.

# 3. newInterval overlaps with this interval:
# Expand newInterval to cover ranges of both interval and old newInterval.
# By continuously merging if needed and stopping early if newInterval is added, we solve problem in 1 pass.
# newInterval is "alive" throughout the loop. It keeps growing as it merges with overlapping intervals.
# We don't know its final size till we're completely done merging and whole loop ends.

# Time: O(n), Space: O(1) auxiliary, O(n) output list
def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    ans = []

    for i in range(len(intervals)):
        # 1. newInterval ends before this interval:
        if newInterval[1] < intervals[i][0]:
            ans.append(newInterval)
            return ans + intervals[i:]

        # 2. newInterval starts after this interval:
        elif newInterval[0] > intervals[i][1]:
            ans.append(intervals[i])

        # 3. newInterval overlaps with this interval:
        else:
            newInterval = [
                min(newInterval[0], intervals[i][0]), # min of 1st value of both
                max(newInterval[1], intervals[i][1])  # max of 2nd value of both
            ]
    ans.append(newInterval)

    return ans

# 2. Binary Search + Merge Intervals: 2-pass solution
# Time: O(n), Space: O(1) auxiliary, O(n) for output list.
def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    ans = []

    # 1. LOWER BOUND Binary Search for insertion index
    l, r = 0, len(intervals)
    while l < r:
        mid = (l + r) // 2
        if intervals[mid][0] < newInterval[0]:
            l = mid + 1
        else:
            r = mid

    intervals.insert(l, newInterval)

    # 2. Merge Intervals: same algorithm as 056_merge_intervals.py
    for int in intervals:
        # if ans is empty or NO overlap between last interval + new interval
        if not ans or ans[-1][1] < int[0]:
            ans.append(int)
        else:  # OVERLAP between last interval + new interval
            ans[-1][1] = max(ans[-1][1], int[1])

    return ans


if __name__ == "__main__":
    assert insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert insert([[1, 3], [4, 6]], [2, 5]) == [[1, 6]]
    assert insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [
        [1, 2],
        [3, 10],
        [12, 16],
    ]
    assert insert([[1, 2], [3, 5], [9, 10]], [6, 7]) == [
        [1, 2],
        [3, 5],
        [6, 7],
        [9, 10],
    ]
    print("All tests passed!")

_______________
Greedy solution example:

intervals: [[1,2], [3,5], [6,7], [8,10]]
new: [4,9]

Initially
ans = []
new = [4,9]

Interval 1: [1,2]

Picture:
[1,2]      [4,9]

Case 2: newInterval is AFTER current interval

So we know [1,2] can never merge with anything later. Append it.

ans = [[1,2]]

Interval 2: [3,5]

Picture:
     [3,5]
       [4,9]
They overlap.

Don't append anything. Instead, enlarge newInterval.

new = [3,9]
ans is still [[1,2]]

Interval 3: [6,7]

Still overlaps. Merge.
new = [3,9]
Nothing changes.
Still don't append newInterval.

Interval 4: [8,10]

Still overlaps. Merge.
new =[3,10]
Still don't append it.
Loop ends.

Now we finally know
newInterval = [3,10] is complete.
Append it.

ans.append(newInterval)

ans = [[1,2],[3,10]]
