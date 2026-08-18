# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/
# https://algo.monster/liteproblems/2461

# Time: O(n), Space: O(k)
def maximumSubarraySum(nums: list[int], k: int) -> int:
    max_sum = window_sum = 0

    # Why do we add possible duplicates to window_sum, not exclude them first?
    # Because sliding window must always represent exactly k consecutive elements from original array.
    # Duplicates aren't valid answers.
    # We temporarily track window_sum because it belongs to current physical window.
    # It's len(freq) == k that checks if this window_sum is valid.

    # Use frequency hashmap---not set---to track distinct nums.
    # Set doesn't track if other copies of that duplicate num remain.
    freq = {}
    for n in nums[:k]:
        window_sum += n
        freq[n] = freq.get(n, 0) + 1

    if len(freq) == k:  # nums[:k] has no duplicates. This is a valid window_sum!
        max_sum = window_sum

    for i in range(k, len(nums)):
        # Slide the fixed-size window forward:
        # Add entering value and remove leaving value.
        # Do this even if the window now has duplicates.
        new, old = nums[i], nums[i - k]
        window_sum += new - old
        freq[new] = freq.get(new, 0) + 1
        freq[old] -= 1
        if freq[old] == 0:
            del freq[old]

        if len(freq) == k:  # window has no duplicates. This is valid window_sum!
            max_sum = max(max_sum, window_sum)

    return max_sum

if __name__ == "__main__":
    assert maximumSubarraySum([1,5,4,2,9,9,9], 3) == 15
    assert maximumSubarraySum([4,4,4], 3) == 0
    assert maximumSubarraySum([1,2,2], 2) == 3
    assert maximumSubarraySum([1,1,1,7,8,9], 3) == 24
    print("All tests passed!")
