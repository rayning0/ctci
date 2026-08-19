# https://leetcode.com/problems/permutation-in-string/description/
# https://neetcode.io/solutions/permutation-in-string
# Return True if one of s1's permutations is a substring of s2.
# Fixed Sliding Window

# Same answer as https://github.com/rayning0/ctci/blob/master/neetcode/438_find_all_anagrams_in_string.py

# Time: O(m + n), Space: O(1)
# It's O(1) space since s1, s2 may only be lowercase English letters.
# freq1, freq2 are O(26) = O(1)
def checkInclusion(s1: str, s2: str) -> bool:
    freq1, freq2 = {}, {}
    ans = False
    k = len(s1)

    for c in s1:
        freq1[c] = freq1.get(c, 0) + 1

    for c in s2[:k]:
        freq2[c] = freq2.get(c, 0) + 1

    if freq2 == freq1:
        return True

    for i in range(k, len(s2)):
        new, old = s2[i], s2[i - k]
        freq2[new] = freq2.get(new, 0) + 1
        freq2[old] -= 1
        if freq2[old] == 0:
            del freq2[old]

        if freq2 == freq1:
            return True

    return ans

if __name__ == "__main__":
    assert checkInclusion("ab", "eidbaooo") == True
    assert checkInclusion("ab", "eidboaoo") == False
    assert checkInclusion("abc", "lecabee") == True
    assert checkInclusion("abc", "lecaabee") == False
    print("All tests passed!")
