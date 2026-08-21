# https://leetcode.com/problems/binary-search/?envType=problem-list-v2&envId=plakya4j
# https://neetcode.io/problems/binary-search/question?list=neetcode150
# Binary Search. Data structure must be SORTED (or monotonic).

# Time: O(log n), Space: O(1)
def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:   # use "l <= r" if we seek target in CLOSED interval [l, r]
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1     # do NOT use l +=1, which is O(n). mid eliminates half of search space, O(log n).
        elif nums[mid] > target:
            r = mid - 1     # do NOT use r -= 1
        else:
            return mid

    return -1

if __name__ == "__main__":
    assert search([5], 5) == 0
    assert search([-1, 0, 3, 5, 9], 9) == 4  # tricky for odd size
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert search([-1, 0, 2, 4, 6, 8], 4) == 3
    assert search([-1, 0, 2, 4, 6, 8], 3) == -1
    print("All tests passed!")

# Use "while l < r" if we seek a BOUNDARY or INSERTION index, not exact match.
# Ex: In these cases , l naturally converges to answer without extra bookkeeping.
# 1. lower bound: first element >= target
# 2. Upper bound: first element > target
# 3. Search insert position
# https://leetcode.com/problems/search-insert-position/description/

# Goal                                  Use
# Is target in array? (Exact match)     [l, r] with l <= r
# Where should target go (Boundary)     [l, r) with l < r
# With [l, r), when loop ends, l is answer. It points to boundary.
