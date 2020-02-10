// https://www.educative.io/courses/grokking-the-coding-interview/YMzBx1gE5EO
// Find length of longest substring with no repeating characters.

// Time complexity: O(n). Space complexity: O(1) -- limited by 256 unique characters
function solution(str) {
  let [maxLength, start] = [0, 0]
  let freq = {}

  for (let end = 0; end < str.length; end++) {
    let char = str[end]

    if (freq[char]) {
      freq = {}
      freq[char] = 1
      start = end
    } else {
      freq[char] = 1
      let length = end - start + 1
      maxLength = Math.max(maxLength, length)
    }
  }

  return maxLength
}

describe("solution()", () => {
  it("finds length of longest substring with distinct characters", () => {
    expect(solution("aabccbb")).toEqual(3)
    expect(solution("abbbb")).toEqual(2)
    expect(solution("abccde")).toEqual(3)
    expect(solution("abccdeaba")).toEqual(5)
  })
})

// Course Answer:

// function non_repeat_substring(str) {
//   let windowStart = 0,
//     maxLength = 0,
//     charIndexMap = {};

//   // try to extend the range [windowStart, windowEnd]
//   for (let windowEnd = 0; windowEnd < str.length; windowEnd++) {
//     const rightChar = str[windowEnd];
//     // if the map already contains the 'rightChar', shrink the window from the beginning so that
//     // we have only one occurrence of 'rightChar'
//     if (rightChar in charIndexMap) {
//       // this is tricky; in the current window, we will not have any 'rightChar' after its previous index
//       // and if 'windowStart' is already ahead of the last index of 'rightChar', we'll keep 'windowStart'
//       windowStart = Math.max(windowStart, charIndexMap[rightChar] + 1);
//     }
//     // insert the 'rightChar' into the map
//     charIndexMap[str[windowEnd]] = windowEnd;
//     // remember the maximum length so far
//     maxLength = Math.max(maxLength, windowEnd - windowStart + 1);
//   }
//   return maxLength;
// }
