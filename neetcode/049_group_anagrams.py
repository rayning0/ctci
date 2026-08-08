# https://leetcode.com/problems/group-anagrams/?envType=problem-list-v2&envId=plakya4j
# https://neetcode.io/problems/anagram-groups/solution

# 2 strings are anagrams only if they have the same character frequencies.
# For each string s, make character freq list "count":
# 26 integers that count number of a's, b's, c's, etc. in each string.

# Then make hashmap:
# key = character freq list, value = list of all strings with that character freq.
# Since lists may NOT be keys, must convert "count" list to tuple as key.

# Ex: strs = ['aab', 'aba', 'baa', 'abbccc']
# hash = {
#   (2, 1, 0, 0, ..., 0): ['aab', 'aba', 'baa'],
#   (1, 2, 3, 0, ..., 0): ['abbccc']
# }

# If don't use defaultdict():
# def groupAnagrams(strs: list[str]) -> list[list[str]]:
#     hash = {}
#     for s in strs:
#         count = [0] * 26
#         for c in s:
#             count[ord(c) - ord("a")] += 1

#         key = tuple(count)
#         if key not in hash:
#             hash[key] = []
#         hash[key].append(s)

#     return list(hash.values())


from collections import defaultdict

# Time: O(m*n), Space: O(m)
# m = # of strings, n = length of longest string
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    # key = freq count array, val = [list of strings matching it]
    hash = defaultdict(list)  # default value = []

    # When you create defaultdict, you specify a default_factory (a callable).

    # If key exists: its value is returned.
    # If key does not exist: default_factory is called to generate a default value:
    # list: returns [], str: returns "", int: returns 0

    for s in strs:
        count = [0] * 26  # freq count array for s

        for c in s:
            count[ord(c) - ord("a")] += 1

        # Can't use mutable 'list' as a dict key. list is unhashable!
        # Wrong: hash[count].append(s)
        # Must use immutable type (tuple) as key
        hash[tuple(count)].append(s)

    # hash.values() returns dict_values, not a list.
    # Must change it to list(hash.values()) to return list of lists.
    return list(hash.values())


# Ex: for strs = ["act", "pots", "tops", "cat", "stop", "hat"]
# hash = defaultdict(<class 'list'>, {
#   (1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['act', 'cat'],
#   (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0): ['pots', 'tops', 'stop'],
#   (1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['hat']
# })

if __name__ == "__main__":
    assert groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]) == [
        ["act", "cat"],
        ["pots", "tops", "stop"],
        ["hat"],
    ]
    assert groupAnagrams(["x"]) == [["x"]]
    assert groupAnagrams([""]) == [[""]]
    print("All tests passed!")
