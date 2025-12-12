# https://leetcode.com/problems/meeting-rooms-ii/?envType=company&envId=netflix&favoriteSlug=netflix-all
# https://neetcode.io/problems/meeting-schedule-ii/question?list=neetcode250
# https://www.jointaro.com/interviews/questions/meeting-rooms-ii/?company=netflix

# ******** 2 pointers *******
# Time: O(n log n), Space: O(n)
# def minMeetingRooms(intervals: list[list[int]]) -> int:
#     rooms, max_rooms = 0, 0
#     s, e = 0, 0  # pointers to start/end times

# if not intervals:
#     return 0

#     start = sorted([int[0] for int in intervals]) # sort by start times
#     end = sorted([int[1] for int in intervals])   # sort by end times

#     # for int in intervals:
#     #     start.append(int[0])
#     #     end.append(int[1])
#     # start.sort()
#     # end.sort()

#     while s < len(start):
#         if start[s] < end[e]:
#             # New meeting starts before any ends - need new room
#             rooms += 1
#             s += 1
#         else:
#             Meeting just ended. Free up 1 room.
#             rooms -= 1
#             e += 1
#         max_rooms = max(max_rooms, rooms)

#     #   else:  # start[s] == end[e]
#     # Meeting ends at same time new one starts
#     # Free room first (-1), then next loop will add room back (+1)
#     # Net effect: No change in # of rooms. Room reused.
#             rooms -= 1
#             e += 1

#     return max_rooms


#     [0------------------------30]
#         [5---10]
#                    [15---20]

# ******** min-heap of end times *******
# https://www.designgurus.io/viewer/document/grokking-the-coding-interview/65290ef475ec5d8676c2f17f

# To check if any room is free, just check top element of min-heap
# (earliest meeting end time). If this earliest room isn't free, no other room is free!
# So we must reserve new room.
import heapq


# Time: O(n log n), Space: O(n)
def minMeetingRooms(intervals: list[list[int]]) -> int:
    if not intervals:
        return 0

    # create min-heap
    free_rooms = []

    # sort meetings by start times
    intervals.sort()
    # intervals.sort(key=lambda int: int[0])

    # Add end time of 1st meeting to min-heap.
    heapq.heappush(free_rooms, intervals[0][1])

    # For 2nd, 3rd, 4th, etc... meetings
    for int in intervals[1:]:
        # If current meeting's start time >= earliest end time (top of min-heap):
        if int[0] >= free_rooms[0]:
            #   - A meeting ended! Let's reuse a room.
            #   - Delete earliest end time from heap
            heapq.heappop(free_rooms)

        # Add current meeting's end time to heap
        heapq.heappush(free_rooms, int[1])

    # min-heap size = min # of rooms needed for all meetings
    return len(free_rooms)


# Ex: intervals = [[0, 30], [5, 10], [15, 20]]
#     [0------------------------30]
#         [5---10]
#                    [15---20]

# heap = [30] <--- end time of Meeting #1

# Meeting #2: intervals[1] = [5, 10]
# Is start time (5) >= earliest end time (30)? NO. First meeting is still going.
# heap = [10, 30] <--- Add 2nd meeting end time to min-heap. It rearranges to 10 is earliest end time.

# Meeting #3: intervals[2] = [15, 20]
# Is start time (15) >= earliest end time (10)? YES. A meeting ended.
# heap = [30] <--- Delete earliest end time (10) from heap.
# heap = [20, 30] <--- Add 3rd meeting end time to min-heap. Now 20 is earliest end time.

# Answer: We need at least 2 meeting rooms (length of heap) for all 3 meetings!

if __name__ == "__main__":
    assert minMeetingRooms([[13, 15], [1, 13], [6, 9]]) == 2
    assert minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert minMeetingRooms([[7, 10], [2, 4]]) == 1  # No overlaps
    assert minMeetingRooms([[4, 9]]) == 1  # No overlaps
    assert minMeetingRooms([[13, 15], [1, 13]]) == 1  # No overlaps
    print("All tests passed!")
