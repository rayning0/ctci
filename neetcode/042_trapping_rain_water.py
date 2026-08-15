# https://leetcode.com/problems/trapping-rain-water/
# https://neetcode.io/problems/trapping-rain-water/solution
# Short video on Dynamic Prog: https://youtube.com/shorts/8oaveMUNlS8?si=5mZG70KD1WoUFXpm

# KEY INSIGHT: water[i] = min(lmax, rmax) - height[i]

# 1. 2 Pointers
# Time: O(n), Space: O(1) <--- BEST!

# Water at position i depends on SHORTER wall between left and right sides.
# As we move both pointers inwards, track highest wall seen on each side (left_max, right_max).

# Moving left -> right, if left wall is lower, left side determines water level.
# left_max - height[l] = trapped water on left.
# Moving right -> left, if right wall is lower, right side determines water level.
# right_max - height[r] = trapped water on right.

def trap(height: list[int]) -> int:
    left_max = right_max = ans = 0
    l, r = 0, len(height) - 1

    while l < r:
        # move index inward for side with LOWER height.
        # water[i] = min(left_max, right_max) - height[i]

        if height[l] < height[r]:
            left_max = max(left_max, height[l])

            # left -> right, this is water trapped at position l, given left_max so far
            ans += left_max - height[l]
            l += 1
        else:
            right_max = max(right_max, height[r])

            # right -> left, this is water trapped at position r, given right_max so far
            ans += right_max - height[r]
            r -= 1

    return ans


# 2. Dynamic Programming
# Make 2 arrays:
# lmax = max wall height from left side to i. Precompute it.
# rmax = max wall height from right side to i. Precompute it.
# Loop over height[i] to add to ans (amount of water at each i):
# water[i] = min(lmax, rmax) - height[i]
# Time: O(n), Space: O(n)
def trap(height: list[int]) -> int:
    size = len(height)
    lmax, rmax = [0]*size , [0]*size
    left_max, right_max = 0, 0
    ans = 0
    # water = [0]*size

    for i in range(size):
        left_max = max(left_max, height[i])
        lmax[i] = left_max

    for i in range(size - 1, -1, -1):
        right_max = max(right_max, height[i])
        rmax[i] = right_max

    for i in range(size):
        ans += min(lmax[i], rmax[i]) - height[i]
        # water[i] = min(lmax[i], rmax[i]) - height[i]

    print(f"height: {height}")
    print(f"lmax:   {lmax}")
    print(f"rmax:   {rmax}")
    # print(f"water:  {water}")
    print()

    return ans

if __name__ == "__main__":
    assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert trap([4,2,0,3,2,5]) == 9
    assert trap([0,2,0,3,1,0,1,3,2,1]) == 9
    print("All tests passed!")

# height: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# lmax:   [0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
# rmax:   [3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1]
# water:  [0, 0, 1, 0, 1, 2, 1, 0, 0, 1, 0, 0]

# height: [4, 2, 0, 3, 2, 5]
# lmax:   [4, 4, 4, 4, 4, 5]
# rmax:   [5, 5, 5, 5, 5, 5]
# water:  [0, 2, 4, 1, 2, 0]

# height: [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
# lmax:   [0, 2, 2, 3, 3, 3, 3, 3, 3, 3]
# rmax:   [3, 3, 3, 3, 3, 3, 3, 3, 2, 1]
# water:  [0, 0, 2, 0, 2, 3, 2, 0, 0, 0]
