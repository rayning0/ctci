# https://leetcode.com/problems/insert-interval/
# https://neetcode.io/solutions/insert-interval (Binary Search)

# Time: O(n), Space: O(n) for output list, O(1) extra space
def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    res = []

    # 1. Binary Search for insertion index
    l, r = 0, len(intervals) - 1
    while l <= r:
        mid = (l + r) // 2
        if intervals[mid][0] < newInterval[0]:
            l = mid + 1
        else:
            r = mid - 1

    intervals.insert(l, newInterval)

    # 2. Merge Intervals: same algorithm as 056_merge_intervals.py
    for int in intervals:
        # if res is empty or NO overlap between last interval + new interval
        if res == [] or res[-1][1] < int[0]:
            res.append(int)
        else:  # OVERLAP between last interval + new interval
            res[-1][1] = max(res[-1][1], int[1])

    return res


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
