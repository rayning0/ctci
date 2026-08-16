# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
# https://neetcode.io/solutions/maximum-number-of-vowels-in-a-substring-of-given-length
# Fixed Sliding Window

# Similar to https://github.com/rayning0/ctci/blob/master/neetcode/643_maximum_average_subarray_i.py

# Time: O(n), Space: O(1)
def maxVowels(s: str, k: int) -> int:
    # lookup for SET is O(1). lookup in list or tuple is O(n). So use SET!
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0

    for c in s[:k]:
        if c in vowels:
            count += 1

    max_vowels = count

    for i in range(k, len(s)):
        if s[i] in vowels:
            count += 1

        if s[i - k] in vowels:
            count -= 1

        max_vowels = max(max_vowels, count)

    return max_vowels

if __name__ == "__main__":
    assert maxVowels("abciiidef", 3) == 3
    assert maxVowels("aeiou", 2) == 2
    assert maxVowels("leetcode", 3) == 2
    print("All tests passed!")
