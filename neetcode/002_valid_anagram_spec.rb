# https://leetcode.com/problems/valid-anagram/?envType=problem-list-v2&envId=plakya4j

# Don't use sort(), since it has time complexity: O(n log n).
# Return false if both s and t are different lengths.
# Make freq hash of each letter in string s.
# Then go through string t, letter by letter.
# If t letter's freq in s > 0, subtract 1 from its freq hash. Else return false.
# If successfully get through all t letters, return true.
# Time: O(n + m), where n = length of s, m = length of t
# Space: O(1)
def is_anagram(s, t)
  return false if s.length != t.length
  freq = Hash.new(0)

  s.each_char do |letter|
    freq[letter] += 1
  end

  t.each_char do |letter|
    if freq[letter] > 0
      freq[letter] -= 1
    else
      return false
    end
  end

  true
end

describe do
  it do
    expect(is_anagram('anagram', 'nagaram')).to eq true
    expect(is_anagram('rat', 'car')).to eq false
    expect(is_anagram('aaaa', 'aaa')).to eq false
  end
end
