# https://leetcode.com/problems/meeting-rooms/
# https://neetcode.io/problems/meeting-schedule/question?list=neetcode250

# Time: O(n log n), Space: O(1)
def canAttendMeetings(intervals: list[list[int]]) -> bool:
    intervals.sort()

    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i + 1][0]:
            return False

    return True


if __name__ == "__main__":
    # OK to say "for i in range(-5))". It skips the loop!
    assert canAttendMeetings([]) == True
    assert canAttendMeetings([[1, 3]]) == True
    assert canAttendMeetings([[0, 30], [5, 10], [15, 20]]) == False
    assert canAttendMeetings([[7, 10], [2, 4]]) == True
    assert canAttendMeetings([[5, 8], [9, 15]]) == True
    print("All tests passed!")
