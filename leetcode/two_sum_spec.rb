# https://leetcode.com/problems/two-sum/

def two_sum(nums, target)
  hash = {}
  nums.each_with_index do |num, i|
    complement = target - num
    if hash[complement]
      return [hash[complement], i]
    end
    hash[num] = i
  end

  raise "No answer"
end

describe "#two_sum" do
  it 'returns indices of two numbers that add up to a specific target' do
    expect(two_sum([2, 7, 11, 15], 9)).to eq [0, 1]
    expect(two_sum([3, 3], 6)).to eq [0, 1]
    expect(two_sum([3, 2, 4], 6)).to eq [1, 2]
  end
end
