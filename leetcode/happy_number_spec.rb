# https://leetcode.com/problems/happy-number/
# Runtime: 28 ms, faster than 98.08% of Ruby online submissions for Happy Number.
# Memory Usage: 9.2 MB, less than 100.00% of Ruby online submissions for Happy Number.

def is_happy(n)
  sums = {}

  while n != 1 do
    sum = 0

    while n != 0 do
      last_digit = n % 10
      sum += last_digit * last_digit
      n /= 10 # remove last digit
    end

    # n.to_s.each_char do |digit|
    #   d = digit.to_i
    #   sum += d * d
    # end

    if sums[sum]
      return false
    else
      sums[sum] = true
    end

    n = sum
  end

  true
end

describe '#is_happy' do
  it 'tells if number is happy' do
    expect(is_happy(19)).to eq true
    expect(is_happy(7)).to eq true
    expect(is_happy(2)).to eq false
    expect(is_happy(9)).to eq false
  end
end
