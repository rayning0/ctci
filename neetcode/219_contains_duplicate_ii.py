# https://leetcode.com/problems/contains-duplicate-ii/
# https://neetcode.io/problems/contains-duplicate-ii/question?list=neetcode250
# Hashmap
# Time: O(n), Space: O(n)
def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    hash = {}
    for j in range(len(nums)):
        # if nums[j] in hash, we already saw nums[j] at earlier i != j
        # hash[nums[j]] is this earlier i.
        if nums[j] in hash and abs(hash[nums[j]] - j) <= k:
            return True
        hash[nums[j]] = j
    return False


if __name__ == "__main__":
    assert containsNearbyDuplicate([1, 2, 3, 1], 3)
    assert containsNearbyDuplicate([1, 0, 1, 1], 1)
    assert not containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)
    print("All tests passed!")


# [1, 0, 1, 1], k = 1
# h = {1: 0, 0: 1}
# j = 2, nums[2] = 1 is in hash and abs(0 - 2) is NOT <= 1
# h = {1: 2, 0: 1}
# j = 3, nums[3] = 1 is in hash and abs(2 - 3) <= 1
# True
# Smallest diff between any 2 duplicate nums is 1 (i = 2, j = 3) <= k, so True

# For [1, 2, 3, 1, 2, 3], k = 2
# Smallest diff between any 2 duplicates is 3 > k, so False

# [1, 2, 3, 1], k = 3
# Smallest diff between any 2 duplicates is 3 <= 3, so True
