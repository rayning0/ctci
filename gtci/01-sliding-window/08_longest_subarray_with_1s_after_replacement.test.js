// https://www.educative.io/courses/grokking-the-coding-interview/B6VypRxPolJ
// Given array with 0s and 1s, if you may replace no more than k 0's with 1's,
// find length of longest contiguous subarray with all 1's.

// Time complexity: O(n). Space complexity: O(1).
function solution(arr, k) {
  let [maxLength, maxOnesCount, start] = [0, 0, 0]

  for (let end = 0; end < arr.length; end++) {
    if (arr[end] == 1) {
      maxOnesCount++
    }

    let length = end - start + 1
    if (length - maxOnesCount > k) {
      if (arr[start] == 1) {
        maxOnesCount--
      }
      start++
    }

    length = end - start + 1
    maxLength = Math.max(maxLength, length)
  }

  return maxLength
}

describe("solution()", () => {
  it("finds length of longest contiguous subarray with all 1's", () => {
    expect(solution([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2)).toEqual(6)
    expect(solution([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3)).toEqual(9)
  })
})
