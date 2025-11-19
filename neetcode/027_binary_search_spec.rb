# https://leetcode.com/problems/binary-search/?envType=problem-list-v2&envId=plakya4j

# Time: O(log n), Space: O(1)
def search(nums, target)
  l, r = 0, nums.size - 1

  while l <= r # need "<=" to solve odd sized arrays
    mid = (l + r) / 2
    if nums[mid] > target
      r -= 1
    elsif nums[mid] < target
      l += 1
    else
      return mid
    end
  end

  -1
end

describe 'binary search' do
  it '' do
    expect(search([5], 5)).to eq 0
    expect(search([-1,0,3,5,9], 9)).to eq 4 # tricky for odd size
    expect(search([-1,0,3,5,9,12], 9)).to eq 4
    expect(search([-1,0,3,5,9,12], 2)).to eq -1
    expect(search([-1,0,2,4,6,8], 4)).to eq 3
    expect(search([-1,0,2,4,6,8], 3)).to eq -1
  end
end
