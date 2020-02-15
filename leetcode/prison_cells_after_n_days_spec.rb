# https://leetcode.com/problems/prison-cells-after-n-days/
# Runtime: 32 ms, faster than 91.67% of Ruby online submissions.
# Memory Usage: 9.6 MB, less than 100.00% of Ruby online submissions.

def prison_after_n_days(cells, n)
  result = Array.new(8, 0)
  n %= 14
  n = 14 if n == 0
  n.times do |i|
    (1..6).each do |col|
      result[col] = cells[col - 1] == cells[col + 1] ? 1 : 0

      # Alternate XOR answer. Runtime 36 ms.
      # result[col] = 1 - cells[col - 1] ^ cells[col + 1]
    end
    cells = result.dup
  end

  result
end

describe "#prison_after_n_days" do
  it 'gives state of prison after n days' do
    expect(prison_after_n_days([0,1,0,1,1,0,0,1], 7)).to eq [0, 0, 1, 1, 0, 0, 0, 0]
    expect(prison_after_n_days([1,0,0,1,0,0,1,0], 1000000000)).to eq [0,0,1,1,1,1,1,0]
  end
end
