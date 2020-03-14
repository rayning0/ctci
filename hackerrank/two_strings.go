// https://www.hackerrank.com/challenges/two-strings/problem
func twoStrings(s1 string, s2 string) string {
    f1 := make(map[rune]int)
    for _, char := range s1 {
        f1[char]++
    }
    for _, char := range s2 {
        if f1[char] > 0 {
            return "YES"
        }
    }
		return "NO"
}
