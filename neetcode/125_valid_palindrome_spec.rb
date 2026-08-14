# https://leetcode.com/problems/valid-palindrome/?envType=problem-list-v2&envId=plakya4j

# Time: O(n), Space: O(1)
def is_palindrome(s)

  # Issue: downcase! returns nil if already lowercase, so &.gsub! never runs
  # Fix: Call gsub! separately, or use downcase (non-bang) which always returns string
  s.downcase!
  s.gsub!(/[[:punct:]\s]/, '') # delete all punctuation + spaces

  (s.size / 2).times do |i|
    return false if s[i] != s[s.size - 1 - i]
  end

  true
end

describe '#is_palindrome' do
  it '' do
    expect(is_palindrome("A man, a plan, a canal: Panama")).to eq true
    expect(is_palindrome("race a car")).to eq false
    expect(is_palindrome(" ")).to eq true
    expect(is_palindrome("a.")).to eq true
  end
end
