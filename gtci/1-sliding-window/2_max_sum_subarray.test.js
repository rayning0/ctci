// https://www.educative.io/courses/grokking-the-coding-interview/JPKr0kqLGNP
// Given array of positive numbers and positive number k,
// find max sum of any contiguous subarray of size k

// Time complexity: O(n). Space complexity: O(1).
function solution(k, arr) {
  let [maxSum, sum, windowStart] = [0, 0, 0]

  for (let windowEnd = 0; windowEnd < arr.length; windowEnd++) {
    sum += arr[windowEnd]
    if (windowEnd >= k - 1) {
      maxSum = Math.max(maxSum, sum)
      sum -= arr[windowStart]
      windowStart++
    }
  }

  return maxSum
}

describe("solution()", () => {
  it("finds max sum of continguous subarray of size k", () => {
    expect(solution(3, [2, 1, 5, 1, 3, 2])).toEqual(9)
    expect(solution(2, [2, 3, 4, 1, 5])).toEqual(7)
  })
})
