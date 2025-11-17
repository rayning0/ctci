# https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=problem-list-v2&envId=plakya4j

# Make hash with each num as key.
# For each num, if num - 1 not in hash, this num is start of new consecutive sequence!
# Start counting length of new sequence and checking for num + 1, num + 2, etc. in hash.
# When hit end of sequence, set max_length and keep looping through nums.
# Time: O(n), Space: O(n)
def longest_consecutive(nums)
  max_length = 0
  nums.uniq! # test cases have many duplicate elements

  # hash = {}
  # nums.each do |num|
  #   hash[num] = true
  # end

  # hash = nums.reduce({}) { |acc, num| acc[num] = true; acc }
  hash = nums.to_h { |num| [num, true] }

  nums.each do |num|
    i = num
    if !hash[i - 1] # num is start of new consecutive sequence
      length = 1

      while hash[i + 1]
        length += 1
        i += 1
      end

      max_length = [max_length, length].max
    end
  end

  max_length
end

describe "" do
  it 'Given integer array, give length of longest consecutive sequence of elements' do
    expect(longest_consecutive([2,20,4,10,3,4,5])).to eq 4
    expect(longest_consecutive([0,3,2,5,4,6,1,1])).to eq 7
    expect(longest_consecutive([100,4,200,1,3,2])).to eq 4
    expect(longest_consecutive([0,3,7,2,5,8,4,6,0,1])).to eq 9
    expect(longest_consecutive([1,0,1,2])).to eq 3
  end
end
