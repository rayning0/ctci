# https://leetcode.com/problems/reverse-string-ii/
# Runtime: 32 ms, faster than 100.00% of Ruby online submissions for Reverse String II.
# Memory Usage: 14.7 MB, less than 100.00% of Ruby online submissions for Reverse String II.

def reverse_str(s, k)
    return s.reverse if k >= s.length
    i, reverse = 0, 1

    while i < s.length do
        if reverse == 1
            if i + k > s.length - 1
                newstr = s[i..s.length - 1].reverse
            else
                newstr = s[i..i + k - 1].reverse + s[i + k..s.length - 1]
            end

            s = i == 0 ? newstr : s[0..i - 1] + newstr
        end

        reverse *= -1
        i += k
    end

    s
end

describe "#reverse_string ii" do
  it 'reverse the first k characters for every 2k characters counting from start of string' do
    expect(reverse_str("abcdefg", 2)).to eq "bacdfeg"
    expect(reverse_str("abcd", 4)).to eq "dcba"
    expect(reverse_str("abcdefg", 8)).to eq "gfedcba"

    expect(reverse_str("hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl", 39)).to eq "fdcqkmxwholhytmhafpesaentdvxginrjlyqzyhehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqllgsqddebemjanqcqnfkjmi"
  end
end
