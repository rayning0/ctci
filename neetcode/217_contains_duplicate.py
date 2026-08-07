# https://leetcode.com/problems/contains-duplicate/description/?envType=problem-list-v2&envId=plakya4j
# https://neetcode.io/problems/duplicate-integer/solution

# Time: O(n), Space: O(n)
def containsDuplicate(nums: list[int]) -> bool:
    seen = set()
    for n in nums:
        if n in seen:
            return True
        else:
            seen.add(n)
    return False

# hashset (set) is better than a hashmap (dict). Comparing both approaches:

# Memory: sets only track membership; dicts store key-value pairs. You don't need the value.
# Semantics: membership checks are clearer with a set.
# Code: seen.add(n) is simpler than seen[n] = True.

# Space complexity: O(n) — same worst case, but sets use less memory per element
# set is more appropriate for membership tracking.

if __name__ == "__main__":
    assert containsDuplicate([1, 2, 3, 1])
    assert not containsDuplicate([1, 2, 3, 4])
    assert containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
    print("All tests passed!")

# Simple tests using assert (no imports needed)
# if __name__ == "__main__": runs code only when the script is run
# directly, not when it's imported as a module.
# When Python runs a file, it sets __name__ to __main__ for that file
# When file is imported, __name__ is set to module name (ex: "001_contains_duplicate")

# Running directly:
# python3 001_contains_duplicate.py
# __name__ == "__main__" is True, so tests run.

# Imported as module in another file:
# from neetcode.001_contains_duplicate import containsDuplicate
# __name__ == "__main__" is False, so tests don't run.

# Why it's useful:
# - Tests run when you execute the file directly
# - Tests don't run when the file is imported elsewhere
# - Keeps the module reusable without side effects
