# https://leetcode.com/problems/string-transforms-into-another-string/
# Runtime: 32 ms, faster than 100.00% of Ruby online submissions for String Transforms Into Another String.
# Memory Usage: 9.9 MB, less than 100.00% of Ruby online submissions for String Transforms Into Another String.
# O(n) time, O(26) space
def convert?(str1, str2)
  return true if str1 == str2
  str1_dictionary = {}  # str1 character maps to str2 character, like cryptography.
  str2_set = Set[]      # Instead of Set, we may use hash and only look at keys
  str1.size.times do |i|
    if str1_dictionary[str1[i]]
      return false if str1_dictionary[str1[i]] != str2[i]
    else
      str1_dictionary[str1[i]] = str2[i]
      str2_set.add(str2[i])
    end
  end

  # If str1 dictionary uses all 26 possible letters but str2 does NOT,
  # it means more than 1 str1 letter maps to the SAME str2 letter.
  # Thus for any unconverted str1 letters, we may use
  if str1_dictionary.keys.size == 26
    return str2_set.size < 26 ? true : false
  end

  true
end

# Imagine an alphabet of a-e (5 letters).

# str1 dictionary = {a: f, b: e, c: d, e: d, g: e, h: d}

# str1 = "bggbehcaaa" (uses 6 unique chars: a, b, c, e, g, h)
# str2 = "eeeedddfff" (uses 3 unique chars)
# bggbchcaaa
# a => f
# bggbehcfff
# e => d
bggbdhcfff
# b => e
eggedhcfff
# c => d
eggedhdfff
# g => e
# eeeedhdfff
# h => d
# eeeedddfff
It's possible to convert from str1 to str2 if:
1. >1 char from str1 maps to same chat in str2
2. str1 and str2 don't share any characters

# abcde
# ecabd

# ebcde
# eccde
# eaade
# eaabe
# daabd

describe "#convert" do
  it 'can convert str1 to str2' do
    expect(convert?("aabcc", "ccdee")).to eq true
    expect(convert?("leetcode", "codeleet")).to eq false
    expect(convert?("abca", "dced")).to eq true
    expect(convert?("ab", "ba")).to eq true
    expect(convert?("aa", "cd")).to eq false
    expect(convert?("ab", "aa")).to eq true
    expect(convert?("abcdefghijklmnopqrstuvwxyz", "bcdefghijklmnopqrstuvwxyza")).to eq false
  end
end
