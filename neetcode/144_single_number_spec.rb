# https://leetcode.com/problems/single-number/?envType=problem-list-v2&envId=plakya4j

# Time: O(n), Space: O(1)
def single_number(nums)
  ans = 0

  nums.each do |num|
    # XOR: https://warrenniu.medium.com/find-the-unique-number-in-an-array-using-the-xor-operator-54d35aa9e8d0
    ans = ans ^ num
  end

  ans
end

describe "#single_number" do
  it 'finds number that appears once in array of numbers where all others appear twice' do
    expect(single_number([2,2,1])).to eq 1
    expect(single_number([4,1,2,1,2])).to eq 4
    expect(single_number([1])).to eq 1
  end
end
