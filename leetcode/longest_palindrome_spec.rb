# https://leetcode.com/problems/longest-palindromic-substring/
# Runtime: 972 ms, faster than 60.50% of Ruby online submissions for Longest Palindromic Substring.
# Memory Usage: 9.3 MB, less than 100.00% of Ruby online submissions for Longest Palindromic Substring.
# O(n * n) time complexity. O(n) space complexity.
def longest(s)
  maxstring = ''

  s.size.times do |i|   # 0 to s.size - 1
    2.times do |j|      # 0 to 1. 0 for odd length palindromes, 1 for even length.
      left = i
      right = i + j

      while left >= 0 && s[left] == s[right] do
        left -= 1
        right += 1
      end

      substring = s[left + 1..right - 1]
      # puts substring
      if substring.size > maxstring.size
        maxstring = substring
      end
    end
  end

  # puts '------------------------'
  maxstring
end

describe '#longest_palindrome' do
  it 'finds longest palindrome substring' do
    expect(longest("aba")).to eq 'aba'
    expect(longest("babad")).to eq 'bab'
    expect(longest("cbbd")).to eq 'bb'
    expect(longest("asdkasdfkxzclxlweieieisweiews")).to eq 'sweiews'
  end
end

# JavaScript:

# var longestPalindrome = function(s) {
#   var max = '';
#   for (var i = 0; i < s.length; i++) {
#     for (var j = 0; j < 2; j++) {
#       var left = i;
#       var right = i + j;
#       while (s[left] && s[left] === s[right]) {
#         left--;
#         right++;
#       }
#       var length = right - left + 1;
#       if (length - 2 > max.length) {
#         max = s.substring(left + 1, right);
#       }
#     }
#   }
#   return max;
# };

# OUTPUT:

# a
# aba
# a
# ------------------------
# b
# bab
# aba
# a
# d
# ------------------------
# c
# b
# bb
# b
# d
# ------------------------
# a
# s
# d
# k
# a
# s
# d
# f
# k
# x
# z
# c
# l
# lxl
# l
# w
# e
# eie
# eieie
# ieiei
# iei
# i
# s
# w
# e
# sweiews
# e
# w
# s
