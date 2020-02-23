# @param {String} s
# @return {String}
def longest(s)
    start = 0
    maxlength = 0
    longest_pal = s[0]
    pals = []

    return s if s.length <= 1

    (0..s.size - 2).each do |i|
      substring2 = s[i..i + 1]
      substring3 = s[i..i + 2]

      if substring2.reverse == substring2
        pals << [i, i + 1]
      end

      if substring3.reverse == substring3
        pals << [i, i + 2]
      end
    end

    pals.each do |start, endindex|
      first, last = start, endindex
      while s[first] == s[last] && first >= 0 && last < s.length
        if s[first..last].length > maxlength
          maxlength = s[first..last].length
          longest_pal = s[first..last]
        end
        first -= 1
        last += 1
      end
    end

    longest_pal
end

describe '#longest_palindrome' do
  it 'tests something' do
    expect(longest("aba")).to eq 'aba'
    expect(longest("babad")).to eq 'bab'
    expect(longest("cbbd")).to eq 'bb'
    expect(longest("asdkasdfkxzclxlweieieisweiews")).to eq 'sweiews'
  end
end
