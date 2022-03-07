// https://leetcode.com/problems/valid-parentheses/
// https://leetcode.com/submissions/detail/654875488/
// Runtime: 64 ms, faster than 91.72% of JavaScript online submissions for Valid Parentheses.
// Memory Usage: 42.7 MB, less than 15.41% of JavaScript online submissions for Valid Parentheses.
// O(n) time, O(n) space
// Time to write code: 5:13 min
// 3 companies asking this: Amazon, LinkedIn, Microsoft
/**
 * @param {string} s
 * @return {boolean}
 */
let isValid = function(s) {
    const parens = {'(': ')', '[': ']', '{': '}'}
    sarray = s.split('')
    let stack = [sarray.shift()] // remove first char of string

    for (let char of sarray) {
        top = stack[stack.length - 1]
        parens[top] === char ? stack.pop() : stack.push(char)
    }

    return stack.length === 0 ? true : false
}
