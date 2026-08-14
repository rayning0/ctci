# https://leetcode.com/problems/valid-palindrome/
# https://neetcode.io/problems/is-palindrome/question

# Time: O(n), Space: O(1)
def isPalindrome(s: str) -> bool:
    clean = ''

    for c in s.lower():     # loop through lowercase version
        if c.isalnum():     # extract alphanumeric characters
            clean += c

    l, r = 0, len(clean) - 1
    while l <= r:
        if clean[l] != clean[r]:
            return False
        l += 1
        r -= 1

    return True

if __name__ == "__main__":
    assert isPalindrome("A man, a plan, a canal: Panama") == True
    assert isPalindrome("race a car") == False
    assert isPalindrome(" ") == True
    assert isPalindrome("Was it a car or a cat I saw?") == True
    print("All tests passed!")
