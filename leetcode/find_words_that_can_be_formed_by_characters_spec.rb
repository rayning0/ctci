# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters
def count_characters(words, chars)
    freq = {}
    good_lengths = 0
    chars.each_char do |char|
        freq[char] ? freq[char] += 1 : freq[char] = 1
    end

    words.each do |word|
        copy = freq.dup
        can_be_made = true
        word.each_char do |char|
            if !copy[char] || copy[char] < 1
                can_be_made = false
                break
            else
                copy[char] -= 1
            end
        end
        good_lengths += word.length if can_be_made
    end

    good_lengths
end

describe "#count_characters" do
  it 'gives sum of lengths of all strings from words array that chars can make' do
    expect(count_characters(["cat","bt","cat","tree"], "atach")).to eq 6
    expect(count_characters(["hello","world","leetcode"], "welldonehoneyr")).to eq 10
  end
end
