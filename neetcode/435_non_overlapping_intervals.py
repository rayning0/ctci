# https://leetcode.com/problems/non-overlapping-intervals/description/
# https://neetcode.io/solutions/non-overlapping-intervals
# Intervals: Sort & Greedy (Keep Smaller End)

# INSIGHT: When intervals overlap, keep the one that ends first.

# Intervals are non-overlapping even if they have a common point.
# Ex: [1, 3] and [2, 4] overlap, but [1, 2] and [2, 3] do not!

# Time: O(n log n), Space: O(1)
def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    intervals.sort()    # O(1) space, since it sorts-in-place
    count = 0
    end = intervals[0][1]

    for i in range(1, len(intervals)):
        # No overlap, so set new end to end of intervals[i]
        if end <= intervals[i][0]:
            end = intervals[i][1]
        else: # Have overlap!

# Set new end to MINIMUM of (end, intervals[i]). Why?
# When 2 intervals overlap, keep interval with SMALLER end time to give the most room
# for future intervals. Interval with bigger end time blocks more upcoming intervals.
            end = min(end, intervals[i][1])
            count += 1

    return count

if __name__ == "__main__":
    assert eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1
    assert eraseOverlapIntervals([[1,2],[1,2],[1,2]]) == 2
    assert eraseOverlapIntervals([[1,2],[2,3]]) == 0
    assert eraseOverlapIntervals([[1,2],[2,4],[1,4]]) == 1
    print("All tests passed!")
