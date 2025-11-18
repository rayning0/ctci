# https://leetcode.com/problems/container-with-most-water/description/?envType=problem-list-v2&envId=plakya4j
# 2 pointers

# Time: O(n), Space: O(1)
def max_area(heights)
  l, r = 0, heights.size - 1
  max_area = 0

  while l < r
    width = r - l
    height = [heights[l], heights[r]].min
    area = width * height
    max_area = [max_area, area].max

    if heights[l] < heights[r]
      l += 1
    else
      r -= 1
    end
  end

  max_area
end

describe "#most water area" do
  it 'find 2 lines that together with x-axis give max area of container' do
    expect(max_area([1,8,6,2,5,4,8,3,7])).to eq 49
    expect(max_area([1,1])).to eq 1
    expect(max_area([1,7,2,5,4,7,3,6])).to eq 36
    expect(max_area([2,2,2])).to eq 4
  end
end
