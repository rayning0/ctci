require 'set'

# O(n) time, O(26) space
def convert?(str1, str2)
  return true if str1 == str2
  dictionary = {}
  set = Set[]
  str1.size.times do |i|
    if dictionary[str1[i]]
      return false if dictionary[str1[i]] != str2[i]
    else
      dictionary[str1[i]] = str2[i]
      set.add(str2[i])
    end
  end

  if dictionary.keys.size == 26
    return set.size < 26 ? true : false
  end

  true
end

# alphabet of a-e (5 letters)

# str1 dictionary = {b: c, c: b, d: a}

# str1 = "aaaabbbccc"
# str2 = "aaaabbbccc"

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
    expect(convert?("abcdefghijklmnopqrstuvwxyz", "bcdefghijklmnopqrstuvwxyza")).to eq false
  end
end
