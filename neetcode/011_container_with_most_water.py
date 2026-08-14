# https://leetcode.com/problems/container-with-most-water/description/?envType=problem-list-v2&envId=plakya4j
# https://neetcode.io/problems/max-water-container/question?list=neetcode150
# 2 pointers

# Time: O(n), Space: O(1)
def maxArea(height: list[int]) -> int:
    l, r = 0, len(height) - 1
    max_area = 0

    while l < r:
        width = r - l
        ht = min(height[l], height[r])
        max_area = max(max_area, width * ht)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_area


if __name__ == "__main__":
    assert maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert maxArea([1, 1]) == 1
    assert maxArea([1, 7, 2, 5, 4, 7, 3, 6]) == 36
    assert maxArea([2, 2, 2]) == 4
    print("All tests passed!")
