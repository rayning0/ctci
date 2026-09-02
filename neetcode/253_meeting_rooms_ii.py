# https://leetcode.com/problems/meeting-rooms-ii/description/
# https://neetcode.io/solutions/meeting-rooms-ii

# Intervals: Sweep Line (2 Pointers)

# 1. 2 Pointers (Sweep Line). EASIEST to remember for interview.
# Time: O(n log n), Space: O(n)
def minMeetingRooms(intervals: list[list[int]]) -> int:
    rooms = max_rooms = 0
    s = e = 0  # pointers to start/end times
    start, end = [], []

    # make sorted arrays of all start times, all end times.
    for int in intervals:
        start.append(int[0])
        end.append(int[1])

    start.sort()
    end.sort()

    while s < len(start):
        if start[s] < end[e]:
            # Meeting just started. Add new room.
            rooms += 1
            s += 1
        else:
            # Meeting just ended. Free a room.
            rooms -= 1
            e += 1
        max_rooms = max(max_rooms, rooms)

    return max_rooms

__________________________________
intervals = [[0,30],[5,10],[15,20]]

    [0------------------------30]
         [5--10]
                 [15--20]

start =[0   5       15]
rooms  +1  +1   -1  +1  -1      -1
end   =        [10      20      30]

if hit a start time, +1 room.
if hit an end time,  -1 room.

# 2. Min Heap of End Times
# https://www.designgurus.io/viewer/document/grokking-the-coding-interview/65290ef475ec5d8676c2f17f

# Check if any room is free now. See top element of min heap (earliest meeting end time).
# If current meeting's start time >= earliest end time,
# a meeting just ended. Reuse a room. Pop earliest end time from heap.
import heapq

# Time: O(n log n), Space: O(n)
def minMeetingRooms(intervals: list[list[int]]) -> int:
    # create min heap
    end_times = []

    # sort meetings by start times
    intervals.sort()

    # Add end time of 1st meeting to min heap.
    heapq.heappush(end_times, intervals[0][1])

    # For later meetings
    for int in intervals[1:]:
        # Is any room free now? If current meeting's start time >= earliest end time (top of min heap):
        if int[0] >= end_times[0]:
            # Meeting just ended. Reuse room with earliest end time. Delete earliest end time from heap.
            heapq.heappop(end_times)

        # Add current meeting's end time to heap.
        # We add end time to heap for ALL meetings, regardless if a room is free now or not.
        heapq.heappush(end_times, int[1])

    # min number of rooms used for all meetings
    return len(end_times)
__________________________________
The heap never shrinks below the number of rooms you've allocated!
Because when you pop, you immediately push.
You're reusing that room.

# Ex: intervals = [[0, 30], [5, 10], [15, 20]]
#     [0------------------------30]
#         [5---10]
#                    [15---20]

heap = [30] <--- end time of Meeting #1

Meeting #2: intervals[1] = [5, 10]
Is start time (5) >= earliest end time (30)? NO. First meeting is still going.
heap = [10, 30] <--- Add 2nd meeting end time to min-heap. It resorts to 10 is earliest end time.

Meeting #3: intervals[2] = [15, 20]
Is start time (15) >= earliest end time (10)? YES. A meeting ended.
heap = [30] <--- Delete earliest end time (10) from heap.
heap = [20, 30] <--- Add 3rd meeting end time to min-heap. Now 20 is earliest end time.

Answer: We need at least 2 meeting rooms (length of heap) for all 3 meetings!

if __name__ == "__main__":
    assert minMeetingRooms([[13, 15], [1, 13], [6, 9]]) == 2
    assert minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert minMeetingRooms([[7, 10], [2, 4]]) == 1    # No overlaps
    assert minMeetingRooms([[4, 9]]) == 1             # No overlaps
    assert minMeetingRooms([[13, 15], [1, 13]]) == 1  # No overlaps
    print("All tests passed!")
