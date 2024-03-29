// https://leetcode.com/problems/valid-anagram/
// https://leetcode.com/submissions/detail/654303346/
// Time to write code: 1:53 min. (Original time to code: 15 min)
// O(n) time, O(n) space
// 3 companies asking this: Bloomberg, Microsoft, Facebook

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
