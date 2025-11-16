# https://neetcode.io/problems/string-encode-and-decode?list=neetcode150
# Use 2 pointers

# ENCODE Complexity:
# Time: O(S) where S = total characters across all strings
#   - strings.map: O(n) iterations where n = number of strings
#   - Per string: O(m) where m = length of string (string concatenation)
#   - Total: O(S) where S = sum of all string lengths
#   - join: O(S) to concatenate all encoded strings
# Space: O(S) for the encoded result string
def encode(strings)
  strings.map { |str| str.length.to_s + '#' + str }.join
end

# DECODE Complexity:
# Time: O(S) where S = length of encoded string = total original characters
#   - Outer while loop: visits each character in encoded string once: O(S)
#   - Inner while loop: finds '#' delimiter - O(1) per string (length digits are small, bounded)
#   - string[i..j-1].to_i: O(1) since length digits are small
#   - string[j+1, length]: O(m) to extract string of length m
#   - Total: O(S) since we process each character exactly once
# Space: O(S) for the result array containing all decoded strings
def decode(string)
  ans = []

  # i jumps from start of each small string ("7#") to the next ("14#")
  i = 0

  while i < string.length
    j = i

    # j first helps find length of small string
    while string[j] != '#'
      j += 1
    end
    length = string[i..j - 1].to_i # length of each small string, from "7#"

    # j helps mark start of each small string to append to answer
    ans << string[j + 1, length]

    # add (length + 1) to j to find start of new "14#" pattern after end of last word
    i = j + length + 1
  end

  ans
end

describe "#encode" do
  it 'encodes (serializes) list of strings into 1 string' do
    expect(encode(["7##neet","code pad loves","love", "", "you"])).to eq "7#7##neet14#code pad loves4#love0#3#you"
    expect(encode(["we","say",":","yes","blah3#howabout this"])).to eq "2#we3#say1#:3#yes19#blah3#howabout this"
  end
end

describe "#decode" do
  it 'decodes (deserializes) 1 string back to original list of strings' do
    expect(decode("7#7##neet14#code pad loves4#love0#3#you")).to eq ["7##neet","code pad loves","love","","you"]
    expect(decode("2#we3#say1#:3#yes19#blah3#howabout this")).to eq ["we","say",":","yes","blah3#howabout this"]
  end
end
