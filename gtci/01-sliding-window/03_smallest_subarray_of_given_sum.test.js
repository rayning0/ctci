// https://www.educative.io/courses/grokking-the-coding-interview/7XMlMEQPnnQ
// Given array of positive numbers and positive number s, find length of smallest
// contiguous subarray whose sum >= s. Return 0 if no such subarray exists.

// Time complexity: O(n). Space complexity: O(1).
function solution(s, arr) {
  let minLength = arr.length + 1
  let [sum, windowStart] = [0, 0]

  for (let windowEnd = 0; windowEnd < arr.length; windowEnd++) {
    sum += arr[windowEnd]

    // In each step, shrink sliding window as small as possible, till sum < s:

    // We do two things in each step:
    // - Keep track of smallest length so far
    // - Subtract window's first element from current sum
    while (sum >= s) {
      const length = windowEnd - windowStart + 1
      minLength = Math.min(minLength, length)
      sum -= arr[windowStart]
      windowStart++
    }
  }

  if (minLength == arr.length + 1) {
    return 0
  }

  return minLength
}

describe("solution()", () => {;
  it("finds length of smallest subarray with a sum >= s", () => {
    expect(solution(7, [2, 1, 5, 2, 3, 2])).toEqual(2)
    expect(solution(7, [2, 1, 5, 2, 8])).toEqual(1)
    expect(solution(8, [3, 4, 1, 1, 6])).toEqual(3)
  })

  it("returns 0 if no smallest subarray found", () => {
    expect(solution(100, [3, 4, 1, 1, 6])).toEqual(0)
  })
})
