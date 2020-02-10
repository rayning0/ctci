// https://www.educative.io/courses/grokking-the-coding-interview/YQQwQMWLx80
// Find length of longest substring in string with <= k distinct characters.

// Time complexity: O(n) where ‘n’ is the number of characters in input string. The outer for loop runs for all characters and inner while loop processes each character only once, thus time complexity = O(n + n), or O(n).

// Space Complexity: O(k), since we store a max of ‘k + 1’ characters in the HashMap.

// Time complexity: O(n). Space complexity: O(k).
function solution(str, k) {
  let [maxLength, start] = [0, 0]

  // A Hashmap in JavaScript is an Object.
  // Difference between Map and Object in JavaScript:
  // https://medium.com/front-end-weekly/es6-map-vs-object-what-and-when-b80621932373
  let freq = {} // frequency hash: # of times each character is in string

  for (let end = 0; end < str.length; end++) {
    let char = str[end]
    freq[char] ? freq[char]++ : freq[char] = 1

    // shrink sliding window until # of distinct chars == k
    while (Object.keys(freq).length > k) {
      let startChar = str[start]
      freq[startChar]--
      if (freq[startChar] == 0) {
        delete freq[startChar]
      }
      start++
    }

    const length = end - start + 1
    maxLength = Math.max(maxLength, length)

    // My Original Answer:

    // distinctChars = Object.keys(freq).length
    // if (distinctChars <= k) {
    //   const length = end - start + 1
    //   maxLength = Math.max(maxLength, length)
    // } else {
    //   let startChar = str[start]
    //   freq[startChar]--
    //   if (freq[startChar] == 0) {
    //     delete freq[startChar]
    //   }
    //   start++
    // }
  }

  return maxLength
}

describe("solution()", () => {
  it("finds length of longest substring with <= k distinct characters", () => {
    expect(solution("cabaaaaabbbc", 2)).toEqual(10)
    expect(solution("araaci", 2)).toEqual(4)
    expect(solution("araaci", 1)).toEqual(2)
    expect(solution("cbbebi", 3)).toEqual(5)
    expect(solution("cbbebi", 10)).toEqual(6)
  })
})
