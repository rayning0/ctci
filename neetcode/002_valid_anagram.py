# https://leetcode.com/problems/valid-anagram/description/?envType=problem-list-v2&envId=plakya4j
# https://neetcode.io/problems/is-anagram/solution
# s, t must be "lowercase English letters"

# 1. HashMap
# Time: O(n + m), Space: O(1) since have at most 26 "lowercase English letters"
from collections import Counter


def validAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    freqS, freqT = Counter(s), Counter(t)

    # freqS, freqT = {}, {}
    # for i in range(len(s)):
    #     # dict.get(key, default) gives value of hashmap if key exists, else gives default
    #     # Most common way to make frequency hashmap:
    #     freqS[s[i]] = freqS.get(s[i], 0) + 1
    #     freqT[t[i]] = freqT.get(t[i], 0) + 1

    return freqS == freqT


# 2. Freq List
# Use size 26 list to count letter freq for each string
# Time: O(n + m), Space: O(1) since have at most 26 "lowercase English letters"
# def validAnagram(s: str, t: str) -> bool:
#     if len(s) != len(t):
#         return False

#     count = [0] * 26  # list of 26 0's
#     for i in range(len(s)):
#         count[ord(s[i]) - ord("a")] += 1
#         count[ord(t[i]) - ord("a")] -= 1

#     for freq in count:
#         if freq != 0:
#             return False

#     return True


# ord(s[i]) - ord("a") converts a lowercase letter to an array index (0–25).
# ord(char) returns the ASCII/Unicode code point of a character
# ord("a") = 97, ord("b") = 98, ord("c") = 99, ..., ord("z") = 122
# Subtracting ord("a") shifts the range to 0–25

if __name__ == "__main__":
    assert validAnagram("anagram", "nagaram")
    assert not validAnagram("rat", "car")
    assert not validAnagram("aaaa", "aaa")
    print("All tests passed!")
