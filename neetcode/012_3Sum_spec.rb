# https://leetcode.com/problems/3sum/description/?envType=problem-list-v2&envId=plakya4j
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# The solution set must not contain duplicate triplets.

# Plan: Sort nums. Fix first element in outer loop. Then run 2nd loop, two-sum remaining nums.
# Since nums is sorted, use 2 pointers to run 2-sum. Each time you find a triplet, move outer pointer in.
# Also, set 2 conditions to avoid duplicate answers.
# Video explanations: https://youtube.com/watch?v=IIxoo93bmPQ
# https://www.youtube.com/watch?v=jzZsG8n2R9A

# Time: O(n^2), Space: O(n)
def three_sum(nums)
  ans = []
  nums.sort!

  nums.each_with_index do |num, i|
    # if new outer loop num is same outer loop num as before, skip to next outer loop num
    next if i > 0 && num == nums[i - 1]

    l = i + 1
    r = nums.size - 1

    while l < r
      sum = num + nums[l] + nums[r]
      if sum > 0
        r -= 1
      elsif sum < 0
        l += 1
      else
        ans << [num, nums[l], nums[r]]

        # move left pointer forward
        l += 1
        # but if its num == previous num for left pointer, keep moving it forward
        while nums[l] == nums[l - 1] && l < r
          l += 1
        end
      end
    end
  end

  ans
end


describe '3 sum' do
  it 'return all triplets where their sum is 0' do
    expect(three_sum([-100,-70,-60,110,120,130,160])).to eq [[-100,-60,160],[-70,-60,130]]
    expect(three_sum([-1,0,1,2,-1,-4])).to eq [[-1,-1,2],[-1,0,1]]
    expect(three_sum([0,1,1])).to eq []
    expect(three_sum([0,0,0])).to eq [[0,0,0]]
  end
end
