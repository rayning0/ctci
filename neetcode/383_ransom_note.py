# https://leetcode.com/problems/ransom-note
from collections import Counter

# Time: O(m + n), Space: O(1). Since we have max 26 lowercase letters, space is O(26) = O(1).

# Make letter freq map for magazine.
# Loop through letters in ransomNote:
# - If ransomNote letter not in freq map, return False
# - Subtract 1 from freq map for that letter
# Since all OK, return True
def canConstruct(ransomNote: str, magazine: str) -> bool:
    freqM = Counter(magazine)
    # if c not in freqM, Counter makes freqM[c] = 0 by default

    for c in ransomNote:
        if freqM[c] <= 0:
            return False
        freqM[c] -= 1

    return True

if __name__ == "__main__":
    assert canConstruct('a', 'b') == False
    assert canConstruct('aa', 'ab') == False
    assert canConstruct('aa', 'aab') == True
    print("All tests passed!")

    # Without "Counter":

    # freqM = {}

    # for c in magazine:
    #     freqM[c] = freqM.get(c, 0) + 1

    # for c in ransomNote:
    #     if c in freqM:
    #         freqM[c] -= 1
    #         if freqM[c] < 0:
    #             return False
    #     else:
    #         return False

    # return True
