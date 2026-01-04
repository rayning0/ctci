# https://leetcode.com/problems/contains-duplicate-iii/description/?envType=company&envId=netflix&favoriteSlug=netflix-all
# https://www.jointaro.com/interviews/questions/contains-duplicate-iii/?company=netflix
# https://algomap.io/question-bank/contains-duplicate-iii

# Given integer array nums and 2 integers indexDiff (k) and valueDiff (t).
# Find a pair of indices (i, j) such that:

# 1. i != j,
# 2. abs(i - j) <= indexDiff.
# 3. abs(nums[i] - nums[j]) <= valueDiff
# Return True/False if this pair exists

# Use SORTED sliding window (l, r pointers) + binary search for insertion.
# window size = indexDiff + 1 ~ k

from sortedcontainers import SortedSet

# Must use SortedSet() for this to run correctly and efficiently:

# Why not plain set?
# Problem: Sets are unordered. Can't do binary search.
# Consequence: You'd have to check every element in the window to see if any falls in the range [nums[r] - valueDiff, nums[r] + valueDiff]
# Time complexity: O(k) per iteration → O(n × indexDiff) worst case
# Result: Time Limit Exceeded on large inputs

# Why not sorted list?
# Problem: While lists are ordered, inserting/removing elements while maintaining sorted order is expensive
# Insertion: O(k) to find position + O(k) to shift elements
# Deletion: O(k) to find element + O(k) to shift elements
# Total: O(n × indexDiff²) worst case → Time Limit Exceeded

# Why SortedSet() works perfectly:
# Maintains sorted order automatically: All operations keep elements sorted
# Insertion: O(log k)
# Deletion: O(log k)
# Binary search (via indexing): O(log k)


# Time: O(n log k), Space: O(k). k = indexDiff
def containsNearbyAlmostDuplicate(
    nums: list[int], indexDiff: int, valueDiff: int
) -> bool:
    window = SortedSet()

    # Must add 1st element to window. We need it for binary search + comparisons later.
    window.add(nums[0])

    l = 0
    for r in range(1, len(nums)):
        # 1. indexDiff: If sliding window too big, move its left side in
        while abs(r - l) > indexDiff:
            window.remove(nums[l])
            l += 1

        # 2. valueDiff: Is any num from window in range nums[r] += valueDiff?
        # Use binary search for insertion index
        low = nums[r] - valueDiff
        high = nums[r] + valueDiff

        bindex = window.bisect_left(low)

        # bisect_left() finds index where new element can be inserted at value while keeping sort order of window. Same as binary search.
        # - If value already there: index returned will be to left of any existing entries of that value. index points to first element in window >=  value.
        # - If value not there: index points to where value would be inserted to keep window sorted. All items to left of returned index < value, and all items to right >= value.
        # Time: O(log n)

        # ---Manual algorithm for bisect_left(). It runs too slowly in LeetCode.---
        # wl, wr = 0, len(window) - 1
        # while wl <= wr:
        #     mid = (wl + wr) // 2
        #     if window[mid] < low:
        #         wl = mid + 1
        #     else:
        #         wr = mid - 1
        # bindex = wl

        if bindex < len(window) and window[bindex] <= high:
            return True
        window.add(nums[r])
    return False


if __name__ == "__main__":
    assert containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0) == True
    assert containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3) == False
    print("All tests passed!")
