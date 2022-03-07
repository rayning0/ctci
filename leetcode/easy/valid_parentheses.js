// https://leetcode.com/problems/valid-parentheses/
// https://leetcode.com/submissions/detail/654870080/
// Runtime: 64 ms, faster than 91.72% of JavaScript online submissions for Valid Parentheses.
// Memory Usage: 42.9 MB, less than 13.93% of JavaScript online submissions for Valid Parentheses.
// Time to write code: 5:13 min
/**
 * @param {string} s
 * @return {boolean}
 */
let isValid = function(s) {
    if (s.length === 1) return false

    const parens = {'(': ')', '[': ']', '{': '}'}
    sarray = s.split('')
    let stack = [sarray.shift()] // remove first char of string

    for (let char of sarray) {
        top = stack[stack.length - 1]
        parens[top] === char ? stack.pop() : stack.push(char)
    }

    return stack.length === 0 ? true : false
}
