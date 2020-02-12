// https://www.educative.io/courses/grokking-the-coding-interview/R8DVgjq78yR
// Given string with lowercase letters, if you may replace no more than k letters
// with any letter, find length of longest repeating substring after replacement.

function solution(str, k) {
  let [maxLength, start, maxFreq] = [0, 0, 0]
  let freq = {}

  for (let end = 0; end < str.length; end++) {
    let rightChar = str[end]
    freq[rightChar] ? freq[rightChar]++ : freq[rightChar] = 1
    maxFreq = Math.max(maxFreq, freq[rightChar])

    let length = end - start + 1
    // console.log(`end: ${end}. substring: "${str.substring(start, end + 1)}"`)
    // console.log(`freq: ${JSON.stringify(freq)}`)
    // console.log(`rightChar: ${rightChar}, freq[${rightChar}]: ${freq[rightChar]}, length: ${length}, maxFreq: ${maxFreq}`)

    // If substring length - maxFreq > k, we've gone beyond limit where
    // we can replace non-rightChars to make a repeating substring.
    if (length - maxFreq > k) {
      // console.log(`length - maxFreq: ${length - maxFreq} > k (${k})`)
      leftChar = str[start]
      freq[leftChar]-- // Since leftChar won't be in our window, drop its freq by 1
      start++          // Shrink sliding window by 1

      // console.log(`New start: ${start}. New freq: ${JSON.stringify(freq)}`)
    }

    length = end - start + 1
    maxLength = Math.max(maxLength, length)
    // console.log(`maxLength: ${maxLength}\n`)
  }

  return maxLength
}

// same answer with no comments
function solution2(str, k) {
  let [maxLength, maxFreq, start] = [0, 0, 0]
  let freq = {}

  for (let end = 0; end < str.length; end++) {
    let rightChar = str[end]
    freq[rightChar] ? freq[rightChar]++ : freq[rightChar] = 1
    maxFreq = Math.max(maxFreq, freq[rightChar])

    let length = end - start + 1
    if (length - maxFreq > k) {
      leftChar = str[start]
      freq[leftChar]--
      start++
    }

    length = end - start + 1
    maxLength = Math.max(maxLength, length)
  }

  return maxLength
}

describe("solution()", () => {
  it("finds length of longest substring with repeating characters, after replacement", () => {
    expect(solution("aabccbb", 2)).toEqual(5)
    expect(solution("abbcb", 1)).toEqual(4)
    expect(solution("abccde", 1)).toEqual(3)
    expect(solution("abccdeacafgca", 3)).toEqual(6)
  })
})

// ------aabccbb--- (k = 2)----

//   end: 0. substring: "a"
// freq: { "a": 1 }
// rightChar: a, freq[a]: 1, length: 1, maxFreq: 1
// maxLength: 1

// end: 1. substring: "aa"
// freq: { "a": 2 }
// rightChar: a, freq[a]: 2, length: 2, maxFreq: 2
// maxLength: 2

// end: 2. substring: "aab"
// freq: { "a": 2, "b": 1 }
// rightChar: b, freq[b]: 1, length: 3, maxFreq: 2
// maxLength: 3

// end: 3. substring: "aabc"
// freq: { "a": 2, "b": 1, "c": 1 }
// rightChar: c, freq[c]: 1, length: 4, maxFreq: 2
// maxLength: 4

// end: 4. substring: "aabcc"
// freq: { "a": 2, "b": 1, "c": 2 }
// rightChar: c, freq[c]: 2, length: 5, maxFreq: 2
// length - maxFreq: 3 > k(2)
// New start: 1. New freq: { "a": 1, "b": 1, "c": 2 }
// maxLength: 4

// end: 5. substring: "abccb"
// freq: { "a": 1, "b": 2, "c": 2 }
// rightChar: b, freq[b]: 2, length: 5, maxFreq: 2
// length - maxFreq: 3 > k(2)
// New start: 2. New freq: { "a": 0, "b": 2, "c": 2 }
// maxLength: 4

// end: 6. substring: "bccbb"
// freq: { "a": 0, "b": 3, "c": 2 }
// rightChar: b, freq[b]: 3, length: 5, maxFreq: 3
// maxLength: 5

// 5
// ------abccdeacafgca--- (k = 3)-- -

//   end: 0. substring: "a"
// freq: { "a": 1 }
// rightChar: a, freq[a]: 1, length: 1, maxFreq: 1
// maxLength: 1

// end: 1. substring: "ab"
// freq: { "a": 1, "b": 1 }
// rightChar: b, freq[b]: 1, length: 2, maxFreq: 1
// maxLength: 2

// end: 2. substring: "abc"
// freq: { "a": 1, "b": 1, "c": 1 }
// rightChar: c, freq[c]: 1, length: 3, maxFreq: 1
// maxLength: 3

// end: 3. substring: "abcc"
// freq: { "a": 1, "b": 1, "c": 2 }
// rightChar: c, freq[c]: 2, length: 4, maxFreq: 2
// maxLength: 4

// end: 4. substring: "abccd"
// freq: { "a": 1, "b": 1, "c": 2, "d": 1 }
// rightChar: d, freq[d]: 1, length: 5, maxFreq: 2
// maxLength: 5

// end: 5. substring: "abccde"
// freq: { "a": 1, "b": 1, "c": 2, "d": 1, "e": 1 }
// rightChar: e, freq[e]: 1, length: 6, maxFreq: 2
// length - maxFreq: 4 > k(3)
// New start: 1. New freq: { "a": 0, "b": 1, "c": 2, "d": 1, "e": 1 }
// maxLength: 5

// end: 6. substring: "bccdea"
// freq: { "a": 1, "b": 1, "c": 2, "d": 1, "e": 1 }
// rightChar: a, freq[a]: 1, length: 6, maxFreq: 2
// length - maxFreq: 4 > k(3)
// New start: 2. New freq: { "a": 1, "b": 0, "c": 2, "d": 1, "e": 1 }
// maxLength: 5

// end: 7. substring: "ccdeac"
// freq: { "a": 1, "b": 0, "c": 3, "d": 1, "e": 1 }
// rightChar: c, freq[c]: 3, length: 6, maxFreq: 3
// maxLength: 6

// end: 8. substring: "ccdeaca"
// freq: { "a": 2, "b": 0, "c": 3, "d": 1, "e": 1 }
// rightChar: a, freq[a]: 2, length: 7, maxFreq: 3
// length - maxFreq: 4 > k(3)
// New start: 3. New freq: { "a": 2, "b": 0, "c": 2, "d": 1, "e": 1 }
// maxLength: 6

// end: 9. substring: "cdeacaf"
// freq: { "a": 2, "b": 0, "c": 2, "d": 1, "e": 1, "f": 1 }
// rightChar: f, freq[f]: 1, length: 7, maxFreq: 3
// length - maxFreq: 4 > k(3)
// New start: 4. New freq: { "a": 2, "b": 0, "c": 1, "d": 1, "e": 1, "f": 1 }
// maxLength: 6

// end: 10. substring: "deacafg"
// freq: { "a": 2, "b": 0, "c": 1, "d": 1, "e": 1, "f": 1, "g": 1 }
// rightChar: g, freq[g]: 1, length: 7, maxFreq: 3
// length - maxFreq: 4 > k(3)
// New start: 5. New freq: { "a": 2, "b": 0, "c": 1, "d": 0, "e": 1, "f": 1, "g": 1 }
// maxLength: 6

// end: 11. substring: "eacafgc"
// freq: { "a": 2, "b": 0, "c": 2, "d": 0, "e": 1, "f": 1, "g": 1 }
// rightChar: c, freq[c]: 2, length: 7, maxFreq: 3
// length - maxFreq: 4 > k(3)
// New start: 6. New freq: { "a": 2, "b": 0, "c": 2, "d": 0, "e": 0, "f": 1, "g": 1 }
// maxLength: 6

// end: 12. substring: "acafgca"
// freq: { "a": 3, "b": 0, "c": 2, "d": 0, "e": 0, "f": 1, "g": 1 }
// rightChar: a, freq[a]: 3, length: 7, maxFreq: 3
// length - maxFreq: 4 > k(3)
// New start: 7. New freq: { "a": 2, "b": 0, "c": 2, "d": 0, "e": 0, "f": 1, "g": 1 }
// maxLength: 6
