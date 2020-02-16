# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
# Dynamic programming
# Runtime: 520 ms, faster than 60.00% of Ruby online submissions for Number of Dice Rolls With Target Sum.
# Memory Usage: 9.7 MB, less than 100.00% of Ruby online submissions for Number of Dice Rolls With Target Sum.

def dice_rolls(d, f, target)
  dp = Array.new(d).map{ |cell| Array.new(target + 1, 0) }

  # fill first row
  (1..target).each do |cell|
    dp[0][cell] = 1 if cell <= f
  end

  (1..d - 1).each do |row|
    (1..target).each do |col|
      (1..f).each do |face_val|
        dp[row][col] += dp[row - 1][col - face_val] if col - face_val >= 0
      end
    end
  end

  dp[d - 1][target] % (10**9 + 7)
end

describe "#dice_rolls" do
  it 'finds # of ways to roll dice so sum == target' do
    expect(dice_rolls(1, 6, 3)).to eq 1
    expect(dice_rolls(2, 6, 7)).to eq 6
    expect(dice_rolls(2, 5, 10)).to eq 1
    expect(dice_rolls(1, 2, 3)).to eq 0
    expect(dice_rolls(3, 5, 7)).to eq 15
    expect(dice_rolls(3, 7, 5)).to eq 6
    expect(dice_rolls(30, 30, 500)).to eq 222616187
  end
end
