// https://www.educative.io/courses/grokking-the-coding-interview/Bn2KLlOR0lQ
// Each character represents a fruit tree. Given 2 baskets, put max # of fruits in
// each basket. Each basket may have only 1 fruit type.
// Once you've started you can’t skip a tree. (Fruits picked must be contiguous.)
// Give max total # of fruits in both baskets.

function solution(arr) {
  let [maxTotalFruits, start] = [0, 0]
  let freq = {} // frequency hash: # of fruits by basket

  for (let end = 0; end < arr.length; end++) {
    let fruit = arr[end]
    freq[fruit] ? freq[fruit]++ : freq[fruit] = 1

    // shrink sliding window until # of distinct fruits == k
    while (Object.keys(freq).length > 2) {
      const startFruit = arr[start]
      freq[startFruit]--
      if (freq[startFruit] == 0) {
        delete freq[startFruit]
      }
      start++
    }

    let totalFruits = end - start + 1 // or Object.values(freq).reduce((a, b) => a + b)
    maxTotalFruits = Math.max(maxTotalFruits, totalFruits)
  }

  return maxTotalFruits
}

describe("solution()", () => {
  it("finds max total # of fruits in both baskets", () => {
    expect(solution(['A', 'B', 'C', 'A', 'C'])).toEqual(3)
    expect(solution(['A', 'B', 'C', 'B', 'B', 'C'], 2)).toEqual(5)
  })
})
