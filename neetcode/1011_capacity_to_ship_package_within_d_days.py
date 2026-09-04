# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
# https://neetcode.io/solutions/capacity-to-ship-packages-within-d-days
# Lower Bound on Answer

# "I'm binary searching the answer. I guess a capacity, simulate the shipping process to see if that capacity is feasible, and because feasibility is monotonic. If a capacity works, every larger capacity also works. I can use a lower-bound binary search to find the smallest feasible capacity."

# Time: O(n log n), Space: O(1)
def shipWithinDays(weights: list[int], days: int) -> int:
    # smallest weight capacity (cap) of ship = max(weights), otherwise can't ship heaviest package
    # biggest weight capacity of ship = sum of all weights
    l, r = max(weights), sum(weights)

    while l < r:
        cap = (l + r) // 2
        # print(f"cap: {cap}, l: {l}, r: {r}")

        days_used = 1
        wsum = 0
        # warr = []

        for w in weights:
            if wsum + w > cap:
                # print(f"Day: {days_used}, wsum: {wsum}, warr: {warr}")
                days_used += 1
                wsum = 0
                # warr = []

            wsum += w
            # warr.append(w)

        # print(f"Day: {days_used}, wsum: {wsum}, warr: {warr}")

        if days_used <= days:
            # print(f"Capacity {cap} valid. Checking if smaller capacity works.")
            # This finds LOWER BOUND, the smallest capacity that works.
            r = cap
        else:
            # print(f"Capacity {cap} too small. Raising it.")
            l = cap + 1

    # print(f"\nFinal ship capacity: {l}")
    return l


if __name__ == "__main__":
    assert shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5) == 15
    assert shipWithinDays([3,2,2,4,1,4], 3) == 6
    assert shipWithinDays([1,2,3,1,1], 4) == 3
    assert shipWithinDays([2,4,6,1,3,10], 4) == 10
    assert shipWithinDays([1,2,3,4,5], 5) == 5
    assert shipWithinDays([1,5,4,4,2,3], 3) == 8
    print("All tests passed!")

# Ex: weights = [1,2,3,4,5,6,7,8,9,10], days = 5

# cap: 32, l: 10, r: 55
# Day: 1, wsum: 28, warr: [1, 2, 3, 4, 5, 6, 7]
# Day: 2, wsum: 27, warr: [8, 9, 10]
# Capacity 32 valid. Checking if smaller capacity works.
# cap: 21, l: 10, r: 32
# Day: 1, wsum: 21, warr: [1, 2, 3, 4, 5, 6]
# Day: 2, wsum: 15, warr: [7, 8]
# Day: 3, wsum: 19, warr: [9, 10]
# Capacity 21 valid. Checking if smaller capacity works.
# cap: 15, l: 10, r: 21
# Day: 1, wsum: 15, warr: [1, 2, 3, 4, 5]
# Day: 2, wsum: 13, warr: [6, 7]
# Day: 3, wsum: 8, warr: [8]
# Day: 4, wsum: 9, warr: [9]
# Day: 5, wsum: 10, warr: [10]
# Capacity 15 valid. Checking if smaller capacity works. <--- ANSWER!
# cap: 12, l: 10, r: 15
# Day: 1, wsum: 10, warr: [1, 2, 3, 4]
# Day: 2, wsum: 11, warr: [5, 6]
# Day: 3, wsum: 7, warr: [7]
# Day: 4, wsum: 8, warr: [8]
# Day: 5, wsum: 9, warr: [9]
# Day: 6, wsum: 10, warr: [10]
# Capacity 12 too small. Raising it.
# cap: 14, l: 13, r: 15
# Day: 1, wsum: 10, warr: [1, 2, 3, 4]
# Day: 2, wsum: 11, warr: [5, 6]
# Day: 3, wsum: 7, warr: [7]
# Day: 4, wsum: 8, warr: [8]
# Day: 5, wsum: 9, warr: [9]
# Day: 6, wsum: 10, warr: [10]
# Capacity 14 too small. Raising it.

# Final ship capacity: 15
