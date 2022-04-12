// https://leetcode.com/problems/reverse-string/
// https://leetcode.com/submissions/detail/678695773/

/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
// 2 pointers: O(n) time, O(1) space
// Companies: Microsoft, Amazon, Apple
// Time to code: 2:56 min
let reverseString = function(s) {
    const len = s.length
    for (let i = 0; i < len / 2; i++) {
      [s[i], s[len - 1 - i]] = [s[len - 1 - i], s[i]] // swap letters
    }
}
