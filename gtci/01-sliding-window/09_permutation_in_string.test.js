// https://www.educative.io/courses/grokking-the-coding-interview/N8vB7OVYo2D
// Given string and a pattern, say if string contains any permutation of the pattern.

// Time complexity: O(n * m). n = str size. m = pattern size.
// Space complexity: O(m)
function solution(str, pattern) {
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
      Object.assign(patternFreq, oldPatternFreq) // Problem: This is O(m)!
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

describe("solution()", () => {
  it("finds if string contains any permutation of a pattern", () => {
    expect(solution("oicbedbcaf", "abc")).toEqual(true)
    expect(solution("oidbcaf", "abc")).toEqual(true)
    expect(solution("odicf", "dc")).toEqual(false)
    expect(solution("bcdxabcdy", "bcdyabcdx")).toEqual(true)
    expect(solution("aaacb", "abc")).toEqual(true)
  })
})

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

//----COURSE SOLUTION--------

// function find_permutation(str, pattern) {
//   let windowStart = 0,
//     matched = 0,
//     charFrequency = {};

//   for (i = 0; i < pattern.length; i++) {
//     const chr = pattern[i];
//     if (!(chr in charFrequency)) {
//       charFrequency[chr] = 0;
//     }
//     charFrequency[chr] += 1;
//   }

//   // Our goal is to match all the characters from the 'charFrequency' with the current window
//   // try to extend the range [windowStart, windowEnd]
//   for (windowEnd = 0; windowEnd < str.length; windowEnd++) {
//     const rightChar = str[windowEnd];
//     if (rightChar in charFrequency) {
//       // Decrement the frequency of matched character
//       charFrequency[rightChar] -= 1;
//       if (charFrequency[rightChar] === 0) {
//         matched += 1;
//       }
//     }

//     if (matched === Object.keys(charFrequency).length) {
//       return true;
//     }

//     // Shrink the sliding window
//     if (windowEnd >= pattern.length - 1) {
//       leftChar = str[windowStart];
//       windowStart += 1;
//       if (leftChar in charFrequency) {
//         if (charFrequency[leftChar] === 0) {
//           matched -= 1;
//         }
//         charFrequency[leftChar] += 1;
//       }
//     }
//   }
//   return false;
// }
