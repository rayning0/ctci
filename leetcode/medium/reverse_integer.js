// https://leetcode.com/problems/reverse-integer/
// https://leetcode.com/submissions/detail/678734546/

/**
 * @param {number} x
 * @return {number}
 */
// BEST answer:
// O(log n) time, O(1) space. x has roughly log(x) digits (base 10).
// Runtime: 60 ms, faster than 99.57% of JavaScript online submissions for Reverse Integer.
// Memory Usage: 43.8 MB, less than 72.48% of JavaScript online submissions for Reverse Integer.
// Companies: Adobe, Amazon, Google
let reverse = function(x) {
  let r = 0
  let temp = Math.abs(x)

  while (temp > 0) {
    let last_digit = temp % 10

    // Math.trunc() returns only integer part. Ignores decimal part.
    // Faster than (temp - last_digit) / 10
    temp = Math.trunc(temp / 10)

    r = r * 10 + last_digit
  }

  if (x >= 0) {
    if (r <= 2**31 - 1) return r
  } else {
    if (-r >= -(2**31)) return -r
  }
  return 0
}

// Example of reversing integer with Answer 1:
temp = x = 512
r = 0

last_digit = 512 % 10 = 2
temp = Math.trunc(512 / 10) = 51
r = 0 * 10 + 2 = 2

last_digit = 51 % 10 = 1
temp = Math.trunc(51 / 10) = 5
r = 2 * 10 + 1 = 21

last_digit = 5 % 10 = 5
temp = Math.trunc(5 / 10) = 0
r = 21 * 10 + 5 = 215  <----REVERSED!!!

_______________________________________
// Easiest to remember, but worse Big O
// O(log n) time, O(n) space
// Time to code: 17:15 min
let reverse = function(x) {
    let r = parseInt(String(Math.abs(x)).split('').reverse().join(''))

    if (x >= 0) {
      if (r <= 2**31 - 1) return r
    } else {
      if (-r >= -(2**31)) return -r
    }
    return 0
}
