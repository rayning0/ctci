# 2 pointers
def subsequence?(s, t)
  i, j = 0, 0
  matches = 0

  while i < s.size && j < t.size  do
    if s[i] == t[j]
      matches += 1
      i += 1
    end

    j += 1
  end

  return true if s.size == matches
  false
end

describe "#subsequence" do
  it 'returns if s is subsequence of t' do
    expect(subsequence?('abc', 'ahbgdc')).to eq true
    expect(subsequence?('axc', 'ahbgdc')).to eq false
    expect(subsequence?('', 'ahbgdc')).to eq true
    expect(subsequence?('abc', '')).to eq false
    expect(subsequence?('', '')).to eq true
    expect(subsequence?('abc', 'adabc')).to eq true
    expect(subsequence?('abc', 'aabc')).to eq true
    expect(subsequence?('aabc', 'abc')).to eq false
  end
end
