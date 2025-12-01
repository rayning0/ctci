# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=problem-list-v2&envId=ebdgnf5s
# https://neetcode.io/problems/longest-substring-without-duplicates/question?list=neetcode150
# Use sliding window

# Time: O(n), Space: O(m). n = string length, m = # of unique characters in string
def lengthOfLongestSubstring(s: str) -> int:
    charSet = set()
    l = 0
    max_length = 0

    for r in range(len(s)):
        # Delete all duplicates of current char from set.
        # Shrink sliding window till all duplicates gone.
        while s[r] in charSet:
            # delete left-most char from set to move sliding window forward 1
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        max_length = max(max_length, len(charSet))
        # print(l, r)
        # print(charSet)
        # print(max_length)

    return max_length


if __name__ == "__main__":
    assert lengthOfLongestSubstring("qrsvbspk") == 5
    assert lengthOfLongestSubstring("abcabcbb") == 3
    assert lengthOfLongestSubstring("bbbbb") == 1
    assert lengthOfLongestSubstring("pwwkew") == 3
    assert lengthOfLongestSubstring("zxyzxyz") == 3
    assert lengthOfLongestSubstring("") == 0
    print("All tests passed!")

# s = "pwwkew"

# l, r = 0, 0
# s[r] = p
# set = {p}
# max_length = 0

# l, r = 0, 1
# s[r] = w
# set = {p, w}
# max_length = 2

# l, r = 1, 2
# s[r] = w
# set = {w}
# max_length = 2

# l, r = 1, 3
# s[r] = k
# set = {w, k}
# max_length = 2

# l, r = 1, 4
# s[r] = e
# set = {w, k, e}
# max_length = 3

# l, r = 2, 5
# s[r] = w
# set = {k, e, w}
# max_length = 3
# __________
# 0 0
# {'q'}
# 1
# 0 1
# {'r', 'q'}
# 2
# 0 2
# {'r', 'q', 's'}
# 3
# 0 3
# {'r', 'q', 's', 'v'}
# 4
# 0 4
# {'r', 'b', 'q', 'v', 's'}

# NOT ok substring: "svbsp"! Can't have 2 "s" in sliding window!

# 5
# 3 5
# {'b', 'v', 's'}
# 5
# 3 6
# {'b', 'v', 's', 'p'}
# 5
# 3 7
# {'b', 'v', 's', 'p', 'k'}
# 5
