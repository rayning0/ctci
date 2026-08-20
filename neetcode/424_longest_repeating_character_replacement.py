# https://leetcode.com/problems/longest-repeating-character-replacement/description/
# https://neetcode.io/solutions/longest-repeating-character-replacement

# We want longest window where we can make all characters same, with max k replacements.

# INSIGHT: Sliding window is valid only if:
# window length - maxf (max freq of all char in s) <= k

# While window length - maxf > k, shrink window from left and adjust counts.

# Time: O(n), Space: O(m) <--- m = # of unique chars in s
def characterReplacement(s: str, k: int) -> int:
    max_length = maxf = l = 0
    freq = {}

    for r in range(len(s)):
        freq[s[r]] = freq.get(s[r], 0) + 1
        maxf = max(maxf, freq[s[r]])

        # While window length too long to replace characters, shrink it from left.
        # window length - most frequent count = # character replacements needed
        while (r - l + 1) - maxf > k:
            freq[s[l]] -= 1
            l += 1

        max_length = max(max_length, r - l + 1)

    return max_length

if __name__ == "__main__":
    assert characterReplacement("ABAB", 2) == 4
    assert characterReplacement("AABABBA", 1) == 4
    assert characterReplacement("XYYX", 2) == 4
    assert characterReplacement("AAABABB", 1) == 5
    print("All tests passed!")
