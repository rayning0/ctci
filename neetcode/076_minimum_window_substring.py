# https://leetcode.com/problems/minimum-window-substring/description/
# https://neetcode.io/solutions/minimum-window-substring
# Variable Sliding Window

# Time: O(n + m), Space: O(k) <--- k = # of unique chars in s and t
def minWindow(s: str, t: str) -> str:
    # ----OPTIONAL----
    # if not s or not t:
    #     return ''

    min_str = ''
    freqS, freqT = {}, {}
    l = 0

    min_length = float("inf")

    for c in t:
        freqT[c] = freqT.get(c, 0) + 1

    required = len(freqT) # sliding window must match this many UNIQUE characters from t
    matched = 0

    for r in range(len(s)):
        freqS[s[r]] = freqS.get(s[r], 0) + 1

        # when a char's freq count in sliding window exactly matches t's count
        if s[r] in freqT and freqS[s[r]] == freqT[s[r]]:
            matched += 1

        # when all of t's characters are in sliding window
        while matched == required:
            length = r - l + 1
            if length < min_length:
                min_length = length
                min_str = s[l:r + 1]

            # shrink left side of sliding window
            freqS[s[l]] -= 1

            # a required char dropped below its target freq
            if s[l] in freqT and freqS[s[l]] < freqT[s[l]]:
                matched -= 1

            # ----OPTIONAL----
            # if freqS[s[l]] == 0:
            #     del freqS[s[l]]

            l += 1

    return min_str

if __name__ == "__main__":
    assert minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert minWindow("a", "a") == "a"
    assert minWindow("a", "aa") == ""
    assert minWindow("OUZODYXAZV", "XYZ") == "YXAZ"
    assert minWindow("xyz", "xyz") == "xyz"
    assert minWindow("x", "xy") == ""
    print("All tests passed!")

