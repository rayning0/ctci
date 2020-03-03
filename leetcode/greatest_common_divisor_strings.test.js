// https://leetcode.com/problems/greatest-common-divisor-of-strings/
// str1, str2 must be multiple of output, but they don't need to be multiples of each other
// Runtime: 52 ms, faster than 90.73 % of JavaScript online submissions for Greatest Common Divisor of Strings.
// Memory Usage: 35.4 MB, less than 100.00 % of JavaScript online submissions for Greatest Common Divisor of Strings.

// Euclidean algorithm for Greatest Common Divisor:
// https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
// If A = 0 then GCD(A, B) = B, since the GCD(0, B) = B.
// If B = 0 then GCD(A, B) = A, since the GCD(A, 0) = A.
// GCD(A, B) = GCD(B, A % B)

// Ex: gcd(100, 60) = gcd(60, 100 % 60 = 40) = gcd(40, 60 % 40 = 20) = gcd(20, 40 % 20 = 0) = 20

function gcd(a, b) {
  if (a == 0) return b
  if (b == 0) return a
  if (b > a) [a, b] = [b, a]

  return gcd(b, a % b)
}

// Time: O(n). Space: O(1).
function gcd_strings(str1, str2) {
  let [longer, shorter] = (str1.length > str2.length) ? [str1, str2] : [str2, str1]
  let gcd2 = gcd(str1.length, str2.length)
  // console.log(`GCD: ${gcd2}`)

  for (let i = 0; i < longer.length; i++) {
    j = i % gcd2 // lets index of shorter string start over from 0 when i >= shorter.length
    // console.log(`i: ${i}, longer[i]: ${longer[i]}, j: ${j}, shorter[j]: ${shorter[j]}`)
    if (longer[i] != shorter[j]) { return "" }
  }

  return shorter.substring(0, gcd2)
}

describe ("#gcd_strings", () => {
  it("returns GCD string", () => {
    expect(gcd_strings("A", "AAA")).toEqual("A")
    expect(gcd_strings("AAA", "AAA")).toEqual("AAA")
    expect(gcd_strings("FFB", "FFBFFB")).toEqual("FFB")
    expect(gcd_strings("LEET", "CODE")).toEqual("")
    expect(gcd_strings("CAB", "BABBAB")).toEqual("")
    expect(gcd_strings("A", "A")).toEqual("A")
    expect(gcd_strings("A", "B")).toEqual("")
    expect(gcd_strings("ABCABC", "ABC")).toEqual("ABC")
    expect(gcd_strings("ABCABD", "ABC")).toEqual("")
    expect(gcd_strings("BAB", "BABXBAB")).toEqual("")
    expect(gcd_strings("BAB", "BABAB")).toEqual("")
    expect(gcd_strings("ABA", "ABABA")).toEqual("")
    expect(gcd_strings("ABABAB", "ABAB")).toEqual("AB")
    expect(gcd_strings("ABCABDABCABD", "ABCABD")).toEqual("ABCABD")
    expect(gcd_strings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX")).toEqual("TAUXX")
    expect(gcd_strings("FFBNXKSTFFBNXKSTFFBNXKSTFFBNXKSTFFBNXKST",
      "FFBNXKSTFFBNXKSTFFBNXKSTFFBNXKSTFFBNXKSTFFBNXKSTFFBNXKSTFFBNXKSTFFBNXKST")).toEqual("FFBNXKST")
  })
})

// expect(gcd_strings("ABCABD", "ABC")).toEqual("")
// GCD: 3
// i: 0, longer[i]: A, j: 0, shorter[j]: A
// i: 1, longer[i]: B, j: 1, shorter[j]: B
// i: 2, longer[i]: C, j: 2, shorter[j]: C
// i: 3, longer[i]: A, j: 0, shorter[j]: A
// i: 4, longer[i]: B, j: 1, shorter[j]: B
// i: 5, longer[i]: D, j: 2, shorter[j]: C

// expect(gcd_strings("ABABAB", "ABAB")).toEqual("AB")
// GCD: 2
// i: 0, longer[i]: A, j: 0, shorter[j]: A
// i: 1, longer[i]: B, j: 1, shorter[j]: B
// i: 2, longer[i]: A, j: 0, shorter[j]: A
// i: 3, longer[i]: B, j: 1, shorter[j]: B
// i: 4, longer[i]: A, j: 0, shorter[j]: A
// i: 5, longer[i]: B, j: 1, shorter[j]: B

// expect(gcd_strings("ABCABDABCABD", "ABCABD")).toEqual("ABCABD")
// GCD: 6
// i: 0, longer[i]: A, j: 0, shorter[j]: A
// i: 1, longer[i]: B, j: 1, shorter[j]: B
// i: 2, longer[i]: C, j: 2, shorter[j]: C
// i: 3, longer[i]: A, j: 3, shorter[j]: A
// i: 4, longer[i]: B, j: 4, shorter[j]: B
// i: 5, longer[i]: D, j: 5, shorter[j]: D
// i: 6, longer[i]: A, j: 0, shorter[j]: A
// i: 7, longer[i]: B, j: 1, shorter[j]: B
// i: 8, longer[i]: C, j: 2, shorter[j]: C
// i: 9, longer[i]: A, j: 3, shorter[j]: A
// i: 10, longer[i]: B, j: 4, shorter[j]: B
// i: 11, longer[i]: D, j: 5, shorter[j]: D
