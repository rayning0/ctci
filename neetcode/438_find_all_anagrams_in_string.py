# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
# https://neetcode.io/solutions/find-all-anagrams-in-a-string
# Fixed Sliding Window

# Same answer as https://github.com/rayning0/ctci/blob/master/neetcode/567_permutation_in_string.py

# Time: O(n + m), Space: O(1)
# It's O(1) space since p, s may only be lowercase English letters.
# freqP, freqS are O(26) = O(1)
def findAnagrams(s: str, p: str) -> list[int]:
    ans = []
    freqP, freqS = {}, {}
    k = len(p)
    for c in p:
        freqP[c] = freqP.get(c, 0) + 1

    for c in s[:k]:
        freqS[c] = freqS.get(c, 0) + 1

    if freqS == freqP:
        ans = [0]

    for i in range(k, len(s)):
        new, old = s[i], s[i - k]
        freqS[new] = freqS.get(new, 0) + 1
        freqS[old] -= 1
        if freqS[old] == 0:
            del freqS[old]

        if freqS == freqP:
            ans.append(i - k + 1)  # add START index of fixed sliding window


    return ans

if __name__ == "__main__":
    assert findAnagrams("cbaebabacd", "abc") == [0,6]
    assert findAnagrams("abab", "ab") == [0,1,2]
    print("All tests passed!")
