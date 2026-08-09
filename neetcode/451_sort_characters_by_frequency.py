# https://leetcode.com/problems/sort-characters-by-frequency/
# s may be any upper + lowercase English letters + digits
# n = length of s
# k = # of unique characters in s = max of 62 (# of upper + lowercase letters + digits)

# 1. HashMap, Sort, and Counter. Easiest to remember!

from collections import Counter

# Time: O(n + k log k) = O(n)
# - Putting all characters into Hash is O(n)
# - Sorting all characters from high to low freq is O(k log k)
# - Since k = 62, k log k goes away.
# Space: O(n)
def frequencySort(s: str) -> str:
    ans = []
    freq = Counter(s)

    # For Counter('tree') = Counter({'e': 2, 't': 1, 'r': 1})
    # freq.most_common() = [('e', 2), ('t', 1), ('r', 1)]
    for c, count in freq.most_common():
        ans.append(c * count)
        # letter * freq of letter
        # ex: 'e' * 2 -> 'ee'
    return ''.join(ans)

if __name__ == "__main__":
    assert frequencySort("tree") == "eetr"
    assert frequencySort("cccaaa") == "cccaaa"
    assert frequencySort("Aabb") == "bbAa"
    assert frequencySort("welcometoleetcode") == "eeeeeooollccttwmd"
    print("All tests passed!")

# 2. HashMap, Sort, without Counter. Hard to remember.
# Time: O(n + k log k), Space: O(n)
def frequencySort(s: str) -> str:
    ans = []
    freq = {}

    for c in s:
        freq[c] = freq.get(c, 0) + 1

    # list that sorts freq in reverse by letter count
    char_by_freq = sorted(
        freq.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for c, count in char_by_freq:
        ans.append(c * count)
    return ''.join(ans)

# 3. Frequency Buckets. Hardest to remember.
# Time: O(n) <--- since NO SORTING used, Space: O(n)
def frequencySort(s: str) -> str:
    freq = {}
    buckets = [] # Never say buckets = ans = []!
    ans = []

    for c in s:
        freq[c] = freq.get(c, 0) + 1

    # buckets is list of lists by frequency:
    # buckets[1] = ['w', 'm', 'd'] = all letters with freq of 1
    # buckets has length len(s) + 1, since s could be all 1 letter with frequency len(s)
    for _ in range(len(s) + 1):
        buckets.append([])
    # buckets = [[] for _ in range(len(s) + 1)] means same thing, but hard to remember

    for c, count in freq.items():
        buckets[count].append(c)

    # from highest to lowest letter freq
    for count in range(len(s), 0, -1):
        for c in buckets[count]:
            ans.append(c * count)

    return ''.join(ans)
