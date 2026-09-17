# https://leetcode.com/problems/car-fleet/description/
# https://neetcode.io/solutions/car-fleet
# Stack: Sort + Fleet Merge

# 1. Process closest cars first.
# 2. Assume each car starts a new fleet. Store each car's arrival time at target in stack.
# 3. If it catches the fleet ahead of it, remove that fleet: pop car's time from stack.
# Size of final stack = # of different fleets.

# Time: O(n log n), Space: O(n)
def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    fleet_times = []  # times of cars to reach target that are in DIFFERENT fleets

    # Sort cars in descending order by position:
    # Since a car can only merge with fleet AHEAD of it, process cars from closest to target first.
    for p, s in sorted(zip(position, speed), reverse=True):
        time = (target - p) / s         # time of car to reach target
        fleet_times.append(time)        # assume this car starts a new fleet

        # If time of current car <= time of car in front, current car merges with front car's fleet.
        # Pop current car, since it did NOT start a new fleet.
        if len(fleet_times) >= 2 and time <= fleet_times[-2]:
            fleet_times.pop()

    return len(fleet_times)   # of different fleets


if __name__ == "__main__":
    assert carFleet(12, [10,8,0,5,3], [2,4,1,1,3]) == 3
    assert carFleet(10, [3], [3]) == 1
    assert carFleet(100, [0,2,4], [4,2,1]) == 1
    assert carFleet(10, [1,4], [3,2]) == 1
    assert carFleet(10, [4,1,0,7], [2,2,1,1]) == 3
    print("All tests passed!")
