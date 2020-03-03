// https://leetcode.com/problems/greatest-common-divisor-of-strings/
// str1, str2 must be multiple of output, but they don't need to be multiples of each other
// strategy:
// 1. Make 1 cursors (or pointers), one for each string
// 2. Move both cursors from left to right, comparing characters. if characters differ before we reach end of shorter string, output = ""
// 3. Keep track of string. If see any substring that repeats, treat that as possible output.
// 4. Otherwise, if we hit end of shorter string, use it as possible output against longer string.
// 5. If shorter string is possible output, check if it repeats in longer string. Check if length of longer string is multiple of shorter string length.

// O(n)
function gcd_strings(str1, str2) {
  let [start, end, oldstart] = [0, 0, 0]
  let [longer, shorter] = (str1.length > str2.length) ? [str1, str2] : [str2, str1]
  let output = ""
  let hash = {}

  while (end < shorter.length) {
    if (str1[end] != str2[end]) {
      return ""
    }
    let char = shorter[end]
    char in hash ? hash[char]++ : hash[char] = 1

    if (shorter[start] == char && hash[char] != output.length + 1 && end > 0) {
      oldstart = start
      while (shorter[start] == shorter[end]) {
        start++
        end++
      }
      console.log("* ", shorter.substring(start, end), output, start,end)
      if (shorter.substring(start, end) != output) {
        start = oldstart
      }
      end--
    }
    end++
    output = shorter.substring(start, end)
    console.log(output, start, end)
  }

  start = 0
  while (end < longer.length) {
    console.log(output, start, longer, end)
    if (output[start] != longer[end]) {
      return ""
    }
    start++
    end++
    if (start == output.length) {
      start = 0
    }
  }
  return output
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

    // "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    // "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
  })
})
