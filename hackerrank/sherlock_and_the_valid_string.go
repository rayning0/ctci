// https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
// Valid if:
// -All letters have same frequency freq
// -All have the same frequency freq, except 1 character with frequency of 1 or freq + 1
func isValid(s string) string {
    if len(s) == 1 {
        return "YES"
    }
    f := make(map[rune]int) // freq of each letter
    f2 := make(map[int]int) // freq of each frequency above

    for _, char := range s {
        f[char]++
    }
    for _, freq := range f {
        f2[freq]++
    }
    if len(f2) == 1 { // all letters have same frequency
        return "YES"
    }
    if len(f2) > 2 { // letters have at least 3 different frequencies
        return "NO"
    }

    maxff := 0
    commonFreq := 0
    for num, ff := range f2 {
        if ff > maxff {
            maxff = ff
            commonFreq = num
        }
    }

    for num, ff := range f2 {
        if ff != maxff {
            if ff == 1 && (num == 1 || num == commonFreq + 1) {
                return "YES"
            }
        }
    }

    return "NO"
}
