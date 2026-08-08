# https://leetcode.com/problems/group-anagrams/description/?envType=problem-list-v2&envId=plakya4j

# Brute force:
# 1. Loop through each string. Sort each alphabetically. But this is O(n log n) time complexity.
# 2. Stick each sorted string in hash. If we've seen this sorted string before, add to group array for that sorted string. Total time: O(m * n log n)

# Better:
# 1. Since each string may only be lowercase English letters, use 26-element array to track freq of all letters in each string.
#  size 26 freq array = [1, 0, 1, 1, .... 0] is for string "acd", etc.
# 2. Make hash where key = freq array, value = list of all strings that match this array.
# Ex: [[1, 0, 1, 1, .... 0] => ["acd", "cad", "dac", etc.], [2, 1, 1, 0, .... 0] => ["abac", "caba", "aabc", etc]

# Time: O(m*n), Space: O(m). m = # of strings, n = length of longest string
def group_anagrams(strs)
  # Make hash where all non-existent keys have default value = []
  # Don't use Hash.new([]). It makes SAME single array object as default for all non-existent keys. So changing default array in 1 key changes it for ALL keys.
  h = Hash.new {|hash, key| hash[key] = []}

  strs.each do |str|
    h[freq_array(str)] << str
  end

  h.values
end

def freq_array(str)
  freq = Array.new(26, 0) # make array of 0's, size 26
  str.each_char do |char|
    # Maps ASCII value of each char to index 0-25.
    # Since 'a'.ord = ASCII of 'a' = 97, 'a'.ord - 'a'.ord = 0
    # 'b'.ord = 98, 'b'.ord - 'a'.ord = 1, etc.
    freq[char.ord - 'a'.ord] += 1
  end
  freq
end

describe "#group_anagrams" do
  it 'groups anagrams together in array of strings' do
    expect(group_anagrams(["act","pots","tops","cat","stop","hat"])).to eq [["act", "cat"], ["pots", "tops", "stop"], ["hat"]]
    expect(group_anagrams(["x"])).to eq [["x"]]
    expect(group_anagrams([""])).to eq [[""]]
  end

  it 'makes frequency array of each string' do
    expect(freq_array("banana")).to eq [3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    expect(freq_array("mississippi")).to eq [0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0]
    expect(freq_array("")).to eq [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  end
end
