# https://leetcode.com/problems/car-pooling/description/
# https://neetcode.io/solutions/car-pooling
# Intervals: Sweep Line

# Also see https://github.com/rayning0/ctci/blob/master/neetcode/253_meeting_rooms_ii.py

# Sweep Line with sorted event list
# Time: O(n log n), Space: O(n)
def carPooling(trips: list[list[int]], capacity: int) -> bool:
    events = []
    count = 0       # current # of people in car

    for trip in trips:
        people, start, end = trip
        events.append((start, people))  # (pick up location,  # of people to add)
        events.append((end, -people))   # (drop off location, # of people to subtract)

    events.sort()
    # sorts events list in ascending order by:
    # 1. location, then by
    # 2. people
    # events.sort(key=lambda event: (event[0], event[1]))

    # Python's tuple comparison is already lexicographic:
    # events.sort() and events.sort(key=lambda e: (e[0], e[1])) produce exact same order. The explicit key is unneeded.

    for _, people in events:
        count += people
        if count > capacity:
            return False

    return True


if __name__ == "__main__":
    assert carPooling([[2,1,5],[3,3,7]], 4) == False
    assert carPooling([[2,1,5],[3,3,7]], 5) == True
    assert carPooling([[4,1,2],[3,2,4]], 4) == True
    assert carPooling([[2,1,3],[3,2,4]], 4) == False
    assert carPooling([[7,5,6],[6,7,8],[10,1,6]], 16) == False
    assert carPooling([[3,5,9],[4,2,5],[3,4,6],[9,1,4],[5,6,8],[5,4,6]], 14) == True
    print("All tests passed!")


# 0  1    2   3   4   5   6   7   8   9
#                     3---------------3
#         4-----------4
#                 3-------3
#     9-----------9
#                         5-------5
#                 5-------5
                                          # event:
# At 1, pick up 9 people = 9 in car         (1,  9)
# At 2, pick up 4 people = 13               (2,  4)
# At 4, drop off 9 people = 4               (4, -9)
# At 4, pick up 3 + 5 people = 12           (4,  3), (4, 5)
# At 5, drop off 4 people = 8               (5, -4)
# At 5, pick up 3 people = 11               (5,  3)
# At 6, drop off 3 + 5 people = 3           (6, -3), (6, -5)
# At 6, pick up 5 people = 8                (6,  5)
# At 8, drop off 5 people = 3               (8, -5)
# ____________________________
# For whole trip, we never exceed max capacity of 14.

# events =

# before sort
# [(5, 3), (9, -3), (2, 4), (5, -4), (4, 3), (6, -3), (1, 9), (4, -9), (6, 5), (8, -5), (4, 5), (6, -5)]
# after sort
# [(1, 9), (2, 4), (4, -9), (4, 3), (4, 5), (5, -4), (5, 3), (6, -5), (6, -3), (6, 5), (8, -5), (9, -3)]
