# https://leetcode.com/problems/continuous-subarray-sum
# https://neetcode.io/solutions/continuous-subarray-sum

# Use these 2 problems as reference. This answer combines both solutions:
# https://github.com/rayning0/ctci/blob/master/neetcode/525_contiguous_array.py
# https://github.com/rayning0/ctci/blob/master/neetcode/974_subarray_sums_divisible_by_k.py
# If 2 prefix sums have same "mod k" value (or REMAINDER when divided by k),
# their difference is divisible by k. <-- KEY INSIGHT
# So store all prefix sum remainders in hashmap, with its index.
# If we've seen remainder before + its subarray length >= 2, we have a desired subarray! Return True.

# Time: O(n), Space: O(n)
def checkSubarraySum(nums: list[int], k: int) -> bool:
    prefix = 0
    prefix_sums = {0: -1} # use -1 as start index to calculate subarray length

    for i, n in enumerate(nums):
        prefix += n
        remainder = prefix % k
        if remainder in prefix_sums:
            length = i - prefix_sums[remainder]
            # length is NOT r - l + 1 for sliding window. This is NOT sliding window problem!
            # Sliding window includes indices l and r in subarray.
            # This subarray is from indices l + 1 to r. So here, length = r - l.
            if length >= 2:
                return True
        else:
            # key = remainder, value = index of prefix sum
            prefix_sums[remainder] = i

    return False

if __name__ == "__main__":
    assert checkSubarraySum([0], 1) == False
    assert checkSubarraySum([1,0], 2) == False
    assert checkSubarraySum([23,2,4,6,7], 6) == True
    assert checkSubarraySum([23,2,6,4,7], 6) == True
    assert checkSubarraySum([23,2,6,4,7], 13) == False
    print("All tests passed!")
