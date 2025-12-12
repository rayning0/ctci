# https://leetcode.com/problems/koko-eating-bananas/?envType=company&envId=netflix&favoriteSlug=netflix-all
# https://neetcode.io/problems/eating-bananas/question?list=neetcode250

# You eat k bananas/hour. Each hour, you may pick a pile of bananas and eats k bananas from that pile.
# If pile < k bananas, you may finish eating the pile, but you can not eat from another pile in same hour.

# Each pile of x bananas takes math.ceil(x/k) hours to eat.
# Since h >= len(piles), top limit of k = max(list) = m, since for THAT k, you can clearly eat all piles in len(piles) hours.

# Brute force:
# for k = 1 to max(list)
# find how long it takes to eat all bananas. Return k if time <= h.

# Optimize: Use Binary Search.


import math


# Time: O(n log m), Space: O(1). n = len(list), m = max(list)
def minEatingSpeed(piles: list[int], h: int) -> int:
    # Brute Force:
    # for k in range(1, max(piles) + 1):
    #     total_time = 0
    #     for pile in piles:
    #         total_time += math.ceil(pile / k)
    #     if total_time <= h:
    #         return k

    # Binary Search: Find minimum k where total_time <= h
    l, r = 1, max(piles)
    res = l

    while l <= r:
        mid = (l + r) // 2
        total_time = 0
        for pile in piles:
            total_time += math.ceil(pile / mid)

        if total_time > h:
            # k is too slow, need faster (higher k)
            l = mid + 1
        else:
            res = mid
            # k is valid (total_time <= h), but search left for smaller valid k
            r = mid - 1

    # After loop, l points to minimum valid k, so you could "return l"
    return res


# Simplified version:
# No need for result variable
# No need to initialize result = l
# Just return l at the end
# This is a standard binary search pattern for "find minimum valid value.""
# After binary search, l points to answer.

if __name__ == "__main__":
    assert minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
    assert minEatingSpeed([25, 10, 23, 4], 4) == 25
    assert minEatingSpeed([1, 4, 3, 2], 9) == 2
    print("All tests passed!")
