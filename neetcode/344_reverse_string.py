# https://leetcode.com/problems/reverse-string/description/
# https://neetcode.io/solutions/reverse-string
# 2-pointer: Converge. Modify in place.

# In Python, strings are IMMUTABLE. So if given string "hello", you can't reverse
# directly in place. Must first convert string to list: list("hello").

# ---LeetCode answer---
# Time: O(n), Space: O(1)
# Given list of chars as input
def reverseString(s: list[str]) -> None:
    l, r = 0, len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

# Given string as input
def reverse2(s: str) -> str:
    l, r = 0, len(s) - 1
    chars = list(s)

    while l < r:
        chars[l], chars[r] = chars[r], chars[l]
        l += 1
        r -= 1

    return ''.join(chars)

# VARIATION: Keep punctuation (and spaces) in place, though reverse rest of sentence.
# Time: O(n), Space: O(1) <--- auxiliary. Don't count size of chars.
# Converting the immutable input string to a list, then back to a string needs O(n) space,
# an unavoidable language constraint in Python for string manipulation.
def reverse3(s: str) -> str:
    chars = list(s)

    l, r = 0, len(chars) - 1
    while l < r:
        # c.isalnum() only is for alphanumerics (letters, numbers)
        # No spaces, commas, periods, apostrophes, etc.
        if not chars[l].isalnum():
            l += 1
        elif not chars[r].isalnum():
            r -= 1
        else:
            chars[l], chars[r] = chars[r], chars[l]
            l += 1
            r -= 1

    return ''.join(chars)

if __name__ == "__main__":
    s = ["h","e","l","l","o"]
    reverseString(s)
    assert s == ["o","l","l","e","h"]
    assert reverse2('hello') == 'olleh'

    s = ["H","a","n","n","a","h"]
    reverseString(s)
    assert s == ["h","a","n","n","a","H"]
    assert reverse2('Hannah') == 'hannaH'

    s = "Hi, what's your name and age? Mine's Bob, age 30."
    assert reverse3(s) == "03, egab'o Bsen iMeg adn aem? anru'o yst, ahw iH."
    print("All tests passed!")
