# https://leetcode.com/problems/rotting-oranges/
# strategy:
# 1. find coordinates of all rotten oranges. return in array of arrays.
# 2. while all oranges are NOT rotten
  # 3. loop through all rotten oranges, then search in all 4 directions for adjacent oranges.
  # 4. if not rotten, make adjacent oranges rotten
# otherwise, return -1

# Runtime: 40 ms, faster than 82.67% of Ruby online submissions for Rotting Oranges.
# Memory Usage: 9.5 MB, less than 100.00% of Ruby online submissions for Rotting Oranges.

# Time complexity: O(n * m). Space complexity: O(n * m).
def oranges(arr)
  min = 0
  rotten = find_all_rotten(arr)
  total_oranges = find_total_oranges(arr)
  return 0 if rotten.size == total_oranges

  while rotten.size < total_oranges
    arr, changes = search_all_4_directions(arr, rotten)
    min += 1
    # puts "arr: #{arr}, changes: #{changes}"
    break if changes == 0
    rotten = find_all_rotten(arr)
  end

  if changes == 0 && rotten.size != total_oranges
    return -1
  end

  min
end

def find_total_oranges(arr)
  total_oranges = 0

  (0..arr.size - 1).each do |row|
    (0..arr[0].size - 1).each do |col|
      total_oranges += 1 if arr[row][col] == 1 || arr[row][col] == 2
    end
  end

  total_oranges
end

def find_all_rotten(arr)
  rotten = []
  (0..arr.size - 1).each do |row|
    (0..arr[0].size - 1).each do |col|
      rotten.push([row, col]) if arr[row][col] == 2
    end
  end

  rotten
end

def search_all_4_directions(arr, rotten)
  changes = 0
  rotten.each do |row, col|
    if col + 1 < arr[0].size && arr[row][col + 1] == 1
      arr[row][col + 1] = 2
      changes += 1
    end

    if col - 1 > -1 && arr[row][col - 1] == 1
      arr[row][col - 1] = 2
      changes += 1
    end

    if row + 1 < arr.size && arr[row + 1][col] == 1
      arr[row + 1][col] = 2
      changes += 1
    end

    if row - 1 > -1 && arr[row - 1][col] == 1
      arr[row - 1][col] = 2
      changes += 1
    end
  end

  [arr, changes]
end

describe "#oranges" do
  it 'makes oranges rotten according to rules' do
    expect(oranges([[2,1,1],[1,1,0],[0,1,1]])).to eq 4
    expect(oranges([[2,1,1],[0,1,1],[1,0,1]])).to eq -1
    expect(oranges([[0,2]])).to eq 0
    expect(oranges([[2,1,0,2]])).to eq 1
  end
end
