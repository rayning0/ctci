// https://leetcode.com/problems/valid-anagram/
// https://leetcode.com/submissions/detail/654303346/
// Time to code: 1:53 min

let isAnagram = function(s, t) {
    if (s.length !== t.length) return false
    let freq = {}

    for (let i in s) {
        freq[s[i]] ? freq[s[i]]++ : freq[s[i]] = 1
        freq[t[i]] ? freq[t[i]]-- : freq[t[i]] = -1
    }

    for (let char of t) {
        if (freq[char] !== 0) return false
    }

    return true
}
