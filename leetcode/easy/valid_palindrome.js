// https://leetcode.com/problems/valid-palindrome/
// https://leetcode.com/submissions/detail/678682789/

/**
 * @param {string} s
 * @return {boolean}
 */
// Best answer: 2 pointers
// O(n) time, O(1) space
// Companies: Facebook, Microsoft, Amazon
// Time to code: 18:39 min. Longest time was figuring out regex.
let isPalindrome = function(s) {
    // Regex reference: https://regex101.com
    // \W Matches anything other than a letter, digit or underscore. Same as [^a-zA-Z0-9_]. Thus add "_" to answer.
    // g modifier: global. All matches (don't return after first match)
    // m modifier: multi line. Causes ^ and $ to match the begin/end of each line (not only begin/end of string)
    s = s.toLowerCase().replace(/[\W_]+/gm, '') // delete all punctuation + spaces

    for (let i = 0; i < s.length / 2; i++) {
        if (s[i] !== s[s.length - 1 - i]) return false
    }
    return true
}

// Simplest answer, but uses O(n) time, O(n) space.
// Unfortunately, JavaScript won't let you easily check equality of 2 arrays:
/// https://www.30secondsofcode.org/articles/s/javascript-array-comparison
// Thus I must rejoin them back to strings
let isPalindrome = function(s) {
    s = s.toLowerCase().replace(/[\W_]+/gm, '') // delete all punctuation + spaces

    return (s === s.split('').reverse().join('')) ? true : false
}
