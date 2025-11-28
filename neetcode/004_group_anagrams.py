# https://leetcode.com/problems/group-anagrams/?envType=problem-list-v2&envId=plakya4j
# https://neetcode.io/problems/anagram-groups/solution

# If don't use defaultdict():
# def groupAnagrams(strs: list[str]) -> list[list[str]]:
#     hash = {}
#     for s in strs:
#         count = [0] * 26
#         for c in s:
#             count[ord(c) - ord("a")] += 1

#         if tuple(count) not in hash:
#             hash[tuple(count)] = []
#         hash[tuple(count)].append(s)

#     return list(hash.values())


from collections import defaultdict


# Time: O(m * n), Space: O(m)
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    # key = freq count array, val = [list of strings matching it]
    hash = defaultdict(list)  # default value = []

    # When you create defaultdict, you specify a default_factory (a callable).

    # If the key exists: its value is returned.
    # If the key does not exist: default_factory is called to generate a default value.

    # int: returns 0, list: returns [], str: returns ""

    for s in strs:
        count = [0] * 26  # freq count array for s

        for c in s:
            count[ord(c) - ord("a")] += 1

        # Can't use mutable 'list' as a dict key. list is unhashable!
        # Wrong: hash[count].append(s)
        # Must use immutable type, like tuple, as key
        hash[tuple(count)].append(s)

    # hash.values() returns dict_values, not a list — Change to return list(hash.values()) to return list of lists.
    return list(hash.values())


if __name__ == "__main__":
    assert groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]) == [
        ["act", "cat"],
        ["pots", "tops", "stop"],
        ["hat"],
    ]
    assert groupAnagrams(["x"]) == [["x"]]
    assert groupAnagrams([""]) == [[""]]
    print("All tests passed!")
