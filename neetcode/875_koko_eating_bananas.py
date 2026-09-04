# https://leetcode.com/problems/koko-eating-bananas/?envType=company&envId=netflix&favoriteSlug=netflix-all
# https://neetcode.io/problems/eating-bananas/question?list=neetcode250
# Lower Bound on Answer

# We eat k bananas/hour. Each hour, we may pick a pile of bananas and eat k bananas from that pile.
# If pile < k bananas, we finish eating that pile but may not eat from another pile in same hour.
# Find min integer k so we can eat ALL bananas in h hours.

# INSIGHT: Each pile of p bananas takes math.ceil(p/k) hours to eat!
# Since h >= len(piles), top limit of k = max(piles) = m, since for that k,
# we can clearly eat all piles in len(piles) = n hours.

# Ex: piles = [3,6,7,11], h = 8

# k = 11 bananas/hr. It takes 4 hrs = len(piles) to eat all bananas. k is too high.
# We won't ever try k > max(piles) = 11.
# hour    bananas left
# ----    ------------
# 0       [3,6,7,11]
# 1       [3,6,7, 0]
# 2       [3,6,0, 0]
# 3       [3,0,0, 0]
# 4       [0,0,0, 0]

# k = 4 bananas/hr.
# hour    bananas left
# ----    ------------
# 0       [3,6,7,11] <-- takes math.ceil(3/4) = 1  hour to eat  3 bananas
# 1       [0,6,7,11] <-- takes math.ceil(6/4) = 2 hours to eat  6 bananas
# 2       [0,2,7,11]
# 3       [0,0,7,11] <-- takes math.ceil(7/4) = 2 hours to eat  7 bananas
# 4       [0,0,3,11]
# 5       [0,0,0,11] <-- takes math.ceil(11/4) = 3 hours to eat 11 bananas
# 6       [0,0,0, 7]
# 7       [0,0,0, 3]
# 8       [0,0,0, 0] <== total = 1 + 2 + 2 + 3 = 8 hours


import math

# Time: O(n log m). n = len(piles), m = max(piles)
# Space: O(1)
def minEatingSpeed(piles: list[int], h: int) -> int:
    # slowest speed must be at least 1 banana/hour.
    # fastest speed must be max(piles) bananas/hour. No point to eat faster.
    l, r = 1, max(piles)

    while l < r:
        k = (l + r) // 2

        hours = 0
        for p in piles:
            hours += math.ceil(p / k)

        if hours <= h:  # k works, but keep checking if SLOWER speed k also works.
            r = k
        else:           # Too slow. Raise speed (k bananas/hour).
            l = k + 1

    return l

# LOWER BOUND does not always mean “check hours >= target.”
# More general meaning: Find first candidate for which a monotonic condition becomes true.
# Find lower bound, the smallest speed k that works.

# Brute Force:

# for k = 1 to max(list)
# find how long it takes to eat all bananas. Return k if time <= h.

# import math

# Time: O(n * m), Space: O(1). n = len(piles), m = max(piles)
# def minEatingSpeed(piles: list[int], h: int) -> int:
    # for k in range(1, max(piles) + 1):
    #     hours = 0
    #     for p in piles:
    #         hours += math.ceil(p / k)
    #     if hours <= h:
    #         return k

if __name__ == "__main__":
    assert minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
    assert minEatingSpeed([25, 10, 23, 4], 4) == 25
    assert minEatingSpeed([1, 4, 3, 2], 9) == 2
    print("All tests passed!")
