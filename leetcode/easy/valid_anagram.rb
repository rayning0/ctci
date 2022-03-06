# https://leetcode.com/problems/valid-anagram/
# Runtime: 72 ms, faster than 79.57% of Ruby online submissions for Valid Anagram.
# Memory Usage: 9.9 MB, less than 100.00% of Ruby online submissions for Valid Anagram.
def is_anagram(s, t)
    return false if s.size != t.size
    freq = Hash.new(0)
    s.size.times do |i|
        schar, tchar = s[i], t[i]
        freq[schar] += 1
        freq[tchar] -= 1
    end

    freq.each do |k, v|
        return false if v != 0
    end

    true
end
