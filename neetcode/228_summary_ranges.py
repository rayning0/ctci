# https://leetcode.com/problems/summary-ranges/description/
# Sliding Window

# Time: O(n), Space: O(n)
def summaryRanges(nums: list[int]) -> list[str]:
    res = []
    i = 0

    # outer loop walks the whole range
    while i < len(nums):
        start = nums[i]
        # loop thru all consecutive nums of subrange. check we don't go beyond end.
        while i < len(nums) - 1 and nums[i + 1] == nums[i] + 1:
            i += 1
        end = nums[i]

        if start == end:
            res.append(f"{start}")
            # OR res.append(str(start))
        else:
            res.append(f"{start}->{end}")
        i += 1

    return res


if __name__ == "__main__":
    assert summaryRanges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
    assert summaryRanges([0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]
    assert summaryRanges([5]) == ["5"]
    assert summaryRanges([]) == []
    print("All tests passed!")
