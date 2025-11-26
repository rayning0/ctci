# https://neetcode.io/problems/duplicate-integer/solution

# Time: O(n), Space: O(n)
def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# hashset (Python set) is better than a hashmap (dict). Comparing both approaches:

# Memory: sets only track membership; dicts store key-value pairs. You don't need the value.
# Semantics: membership checks are clearer with a set.
# Code: seen.add(n) is simpler than seen[n] = True.

# Space complexity: O(n) — same worst case, but sets use less memory per element
# set is more appropriate for membership tracking.
