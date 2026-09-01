# https://leetcode.com/problems/merge-intervals/description/?envType=company&envId=netflix&favoriteSlug=netflix-all
# https://neetcode.io/problems/merge-intervals/question?list=neetcode150
# Sort & Greedy Merge

# PLAN: Sort by starting value. Compare each interval only with last merged interval.

# Time: O(n log n), Space: O(n)
def merge(intervals: list[list[int]]) -> list[list[int]]:
    ints = sorted(intervals)
    ans = []
    for int in ints:
        # if ans == [] or NO overlap between last interval + new interval.
        # if 2nd val of last interval < 1st value of new interval
        # Ex: ans = [[2,6]], int = [8,10]
        if not ans or ans[-1][1] < int[0]:
            ans.append(int)

        else:  # OVERLAP! Ex: [[1,3]], int = [2,6] => New ans = [[1, 6]]
            # Change 2nd val of last interval to max of it and 2nd val of new interval. max(3, 6) = 6.
            ans[-1][1] = max(ans[-1][1], int[1])

    return ans


if __name__ == "__main__":
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge([[4, 7], [1, 4]]) == [[1, 7]]
    assert merge([[1, 4]]) == [[1, 4]]
    assert merge([[2,3],[4,5],[6,7],[8,9],[1,10]]) == [[1,10]]
    print("All tests passed!")

Q: Why is sorting intervals first most optimal solution?

Think about what sorting gives you: after sorting by start time, when you process intervals left to right, any future interval can only overlap with the last merged interval in your result. This is because all previous intervals have already been fully "absorbed."

Without sorting, consider this input: [[5,6], [1,4], [3,8]]

Process [5,6] → ans = [[5,6]]
Process [1,4] → no overlap with [5,6], append → ans = [[5,6],[1,4]]
Process [3,8] → overlaps with both [5,6] and [1,4], but you only checked against the last one!
Sorting prevents this by ensuring overlapping intervals are adjacent in order.

Without sorting?
An interval could overlap with any previously processed interval, not just the last one. So you'd need a way to:

- Find all groups of mutually overlapping intervals
- Merge each group into one interval
_________
Order to study these Interval LeetCode problems:

1. Sort & Greedy Merge
- 56 Merge Intervals
- 57 Insert Interval

Sort by start.
Compare only with the last merged interval.

2. Sort & Conflict Detection
- 252 Meeting Rooms

Sort by start.
Compare neighbors only.

3. Greedy Scheduling
- 435 Non-overlapping Intervals

Sort by end.
Always keep interval that finishes earliest.

This is one of the most important greedy ideas in all of LeetCode.

4. Concurrent Intervals
- 253 Meeting Rooms II

How many intervals overlap at once? Use "sweep line / min heap"

5. Sweep Line
- 1094 Car Pooling
- 2251 Number of Flowers in Full Bloom

Convert interval endpoints into events and process them in order.
