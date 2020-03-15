// https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
// Loop through all possible substrings and make substring frequency map.
// Each substring's frequency has "n choose 2" possible pairs. Loop through each frequency to find sum of all "frequency choose 2".

func sherlockAndAnagrams(s string) int {
    ssmap := make(map[[26]int]int) // substring frequency map

    // loop through all possible substrings
    for start := 0; start < len(s); start++ {
        for end := start; end < len(s); end++ {
            substr := s[start:end + 1]
            ssmap[freqArray(substr)]++
        }
    }
    delete(ssmap, freqArray(s)) // don't count original string s

    numPairs := 0
    for _, freq := range ssmap {
		// Each substring's frequency has "n choose 2" pair combinations.
		// combination("n choose 2") = n!/2!(n-2)! = n(n-1)/2
        numPairs += freq * (freq - 1) / 2
    }

    return numPairs
}

func charToIndex(char rune) int {
    return int(rune(char) - 97)
}
func freqArray(s string) [26]int {
    var freq [26]int
    for _, char := range s {
        i := charToIndex(char)
        freq[i]++
    }
    return freq
}

// func isAnagram(s, t string) bool {
//     if len(s) != len(t) {
//         return false
//     }
//     freq := make(map[rune]int)
//     runes := []rune(s)
//     runet := []rune(t)
//     for i := 0; i < len(runes); i++ {
//         schar := runes[i]
//         tchar := runet[i]
//         freq[schar]++
//         freq[tchar]--
//     }
//     for _, val := range freq {
//         if val != 0 {
//             return false
//         }
//     }
//     return true
// }
