// https://www.educative.io/courses/grokking-the-coding-interview/7XMlMEQPnnQ
// Given array of positive numbers and positive number s, find length of smallest
// contiguous subarray whose sum >= s. Return 0 if no such subarray exists.

// Time complexity: O(n). Space complexity: O(1).
function solution(s, arr) {
  let minLength = arr.length + 1
  let [sum, length] = [0, 0]

  for (let i = 0; i < arr.length; i++) {
    if (sum >= s) {
      minLength = Math.min(minLength, length)
      length--
      sum -= arr[i - length]
    } else {
      sum += arr[i]
      length++
    }
  }

  const lastElem = arr[arr.length - 1]
  if (lastElem >= s) {
    minLength = 1
  }

  if (minLength == arr.length + 1) {
    return 0
  }

  return minLength
}

describe("solution()", () => {
  it("finds length of smallest subarray with a sum >= s", () => {
    expect(solution(7, [2, 1, 5, 2, 3, 2])).toEqual(2)
    expect(solution(7, [2, 1, 5, 2, 8])).toEqual(1)
    expect(solution(8, [3, 4, 1, 1, 6])).toEqual(3)
  })

  it("returns 0 if no smallest subarray found", () => {
    expect(solution(100, [3, 4, 1, 1, 6])).toEqual(0)
  })
})

// COURSE ANSWER:

// function smallest_subarray_with_given_sum(s, arr) {
//   let windowSum = 0,
//     minLength = Infinity,
//     windowStart = 0;

//   for (windowEnd = 0; windowEnd < arr.length; windowEnd++) {
//     windowSum += arr[windowEnd]; // add the next element
//     // shrink the window as small as possible until the 'window_sum' is smaller than 's'
//     while (windowSum >= s) {
//       minLength = Math.min(minLength, windowEnd - windowStart + 1);
//       windowSum -= arr[windowStart];
//       windowStart += 1;
//     }
//   }

//   if (minLength === Infinity) {
//     return 0;
//   }
//   return minLength;
// }
