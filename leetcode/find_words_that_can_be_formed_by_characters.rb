# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters
def count_characters(words, chars)
    freq = {}
    good_lengths = 0
    chars.split('').each do |char|
        freq[char] ? freq[char] += 1 : freq[char] = 1
    end
    old_freq = freq.dup

    words.each do |word|
        good_lengths += word.length
        word.split('').each do |char|
            if freq[char] && freq[char] > 0
                freq[char] -= 1
            else

                good_lengths -= word.length
                break
            end
        end
        freq = old_freq.dup
    end
    good_lengths
end
