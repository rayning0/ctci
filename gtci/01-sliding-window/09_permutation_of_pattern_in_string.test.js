// https://www.educative.io/courses/grokking-the-coding-interview/N8vB7OVYo2D
// Given string and a pattern, find if string contains any permutation of the pattern.

// Time complexity: O(n + m). n = str length. m = pattern length.
// Space complexity: O(m) since in worst case, all pattern's distinct chars may be in HashMap
function solution(str, pattern) {
  let [start, matched] = [0, 0]
  let patternFreq = {}

  for (let i = 0; i < pattern.length; i++) {
    patternFreq[pattern[i]] ? patternFreq[pattern[i]]++ : patternFreq[pattern[i]] = 1
  }

  for (let end = 0; end < str.length; end++) {
    rightChar = str[end]

    if (rightChar in patternFreq) {
      patternFreq[rightChar]--

      // If matched all copies of 1 char from pattern
      if (patternFreq[rightChar] == 0) {
        matched++
      }
    }

    // If match all distinct chars from pattern, we're done!
    if (matched == Object.keys(patternFreq).length) {
      return true
    }

    // If right side of window > pattern length, shrink window for next loop
    if (end >= pattern.length - 1) {
      leftChar = str[start]
      start++

      // If character leaving window was part of pattern:
      // 1. Add it back to frequency HashMap
      // 2. Subtract 1 from matched
      if (leftChar in patternFreq) {
        if (patternFreq[leftChar] === 0) {
          matched--
        }
        patternFreq[leftChar]++
      }
    }
  }

  return false
}

describe("solution()", () => {
  it("finds if string contains any permutation of a pattern", () => {
    expect(solution("oicbedbcaf", "abc")).toEqual(true)
    expect(solution("oidbcaf", "abc")).toEqual(true)
    expect(solution("odicf", "dc")).toEqual(false)
    expect(solution("bcdxabcdy", "bcdyabcdx")).toEqual(true)
    expect(solution("aaacb", "abc")).toEqual(true)
  })
})

//----My Slow Answer--------

// Time complexity: O(n * m). n = str size. m = pattern size.
// Space complexity: O(m)
function slow_solution(str, pattern) {
  let [hasPermutation, start, maxLength] = [false, 0, 0]
  let [patternFreq, oldPatternFreq] = [{}, {}]

  for (let i = 0; i < pattern.length; i++) {
    patternFreq[pattern[i]] ? patternFreq[pattern[i]]++ : patternFreq[pattern[i]] = 1
  }
  Object.assign(oldPatternFreq, patternFreq)

  for (let end = 0; end < str.length; end++) {
    rightChar = str[end]

    if (patternFreq[rightChar]) {
      patternFreq[rightChar]--
    } else {
      start = end + 1
      Object.assign(patternFreq, oldPatternFreq) // Weakness: This is O(m)!
    }

    const length = end - start + 1
    maxLength = Math.max(maxLength, length)

    if (maxLength == pattern.length) {
      hasPermutation = true
      break
    }
  }

  return hasPermutation
}

// Output to my slow answer:
// string: oicbedbcaf, pattern: abc

// patternFreq: { "a": 1, "b": 1, "c": 1 }
// rightChar: o
// start: 0, end: 0, substring: o
// rightChar not in pattern
// maxLength: 0, length: 0

// patternFreq: { "a": 1, "b": 1, "c": 1 }
// rightChar: i
// start: 1, end: 1, substring: i
// rightChar not in pattern
// maxLength: 0, length: 0

// patternFreq: { "a": 1, "b": 1, "c": 1 }
// rightChar: c
// start: 2, end: 2, substring: c
// rightChar in pattern
// maxLength: 1, length: 1

// patternFreq: { "a": 1, "b": 1, "c": 0 }
// rightChar: b
// start: 2, end: 3, substring: cb
// rightChar in pattern
// maxLength: 2, length: 2

// patternFreq: { "a": 1, "b": 0, "c": 0 }
// rightChar: e
// start: 2, end: 4, substring: cbe
// rightChar not in pattern
// maxLength: 2, length: 0

// patternFreq: { "a": 1, "b": 1, "c": 1 }
// rightChar: d
// start: 5, end: 5, substring: d
// rightChar not in pattern
// maxLength: 2, length: 0

// patternFreq: { "a": 1, "b": 1, "c": 1 }
// rightChar: b
// start: 6, end: 6, substring: b
// rightChar in pattern
// maxLength: 2, length: 1

// patternFreq: { "a": 1, "b": 0, "c": 1 }
// rightChar: c
// start: 6, end: 7, substring: bc
// rightChar in pattern
// maxLength: 2, length: 2

// patternFreq: { "a": 1, "b": 0, "c": 0 }
// rightChar: a
// start: 6, end: 8, substring: bca
// rightChar in pattern
// maxLength: 3, length: 3
