# https://leetcode.com/problems/rotting-oranges/
# Runtime: 40 ms, faster than 88.42% of Ruby online submissions for Rotting Oranges.
# Memory Usage: 9.6 MB, less than 100.00% of Ruby online submissions for Rotting Oranges.

# BFS strategy:
# 1. Find all rotten oranges and total fresh oranges. Take first cell off queue.
# 2. While rotten orange queue is NOT empty
    #      For each cell, search neighbors in 4 directions (right, left, down, up)
    #      If neighbor == fresh
        #       5. make it rotten
        #       6. add to queue [neighbor_row, neighbor_col, depth + 1]
        #       7. subtract 1 from # of fresh oranges
# 9. Return depth if fresh == 0
# 10. Return -1

FRESH, ROTTEN = 1, 2

# Time complexity: O(n * m). Space complexity: O(n * m).
def find_rotten_fresh(arr)
  rotten, fresh = [], 0
  arr.size.times do |row|
    arr[0].size.times do |col|
      rotten << [row, col, 0] if arr[row][col] == ROTTEN
      fresh += 1 if arr[row][col] == FRESH
    end
  end
  [rotten, fresh]
end

def oranges(arr)
  depth = 0
  queue, fresh = find_rotten_fresh(arr) # queue has only ROTTEN tomatoes
  height, width = arr.size, arr[0].size
  directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
  max_depth = -1

  while !queue.empty? do
    row, col, depth = queue.shift
    max_depth = [max_depth, depth].max

    directions.each do |drow, dcol|
      nrow = row + drow
      ncol = col + dcol

      if ncol.between?(0, width - 1) && nrow.between?(0, height - 1) && arr[nrow][ncol] == FRESH
        arr[nrow][ncol] = ROTTEN
        queue << [nrow, ncol, depth + 1]
        fresh -= 1
      end
    end
  end

  return depth if fresh == 0
  -1
end

describe "#oranges" do
  it 'makes oranges rotten according to rules' do
    expect(oranges([[2,1,1],[1,1,0],[0,1,1]])).to eq 4
    expect(oranges([[2,1,1],[0,1,1],[1,0,1]])).to eq -1
    expect(oranges([[0,2]])).to eq 0
    expect(oranges([[2,1,0,2]])).to eq 1
    expect(oranges([[1,2,1,1,2,1,1]])).to eq 2
  end
end

# original_queue_size: 1. rotten queue: [[0, 0]]
# cell[0, 0] = 2. queue: []. fresh: 6
# neighbor[0, 1] = 1
# ** [0, 1] turns rotten **
# neighbor[1, 0] = 1
# ** [1, 0] turns rotten **
# depth: 1
# [2, 2, 1]
# [2, 1, 0]
# [0, 1, 1]

# original_queue_size: 2. rotten queue: [[0, 1], [1, 0]]
# cell[0, 1] = 2. queue: [[1, 0]]. fresh: 4
# neighbor[0, 2] = 1
# ** [0, 2] turns rotten **
# neighbor[0, 0] = 2
# neighbor[1, 1] = 1
# ** [1, 1] turns rotten **
# cell[1, 0] = 2. queue: [[0, 2], [1, 1]]. fresh: 2
# neighbor[1, 1] = 2
# neighbor[2, 0] = 0
# neighbor[0, 0] = 2
# depth: 2
# [2, 2, 2]
# [2, 2, 0]
# [0, 1, 1]

# original_queue_size: 2. rotten queue: [[0, 2], [1, 1]]
# cell[0, 2] = 2. queue: [[1, 1]]. fresh: 2
# neighbor[0, 1] = 2
# neighbor[1, 2] = 0
# cell[1, 1] = 2. queue: []. fresh: 2
# neighbor[1, 2] = 0
# neighbor[1, 0] = 2
# neighbor[2, 1] = 1
# ** [2, 1] turns rotten **
# neighbor[0, 1] = 2
# depth: 3
# [2, 2, 2]
# [2, 2, 0]
# [0, 2, 1]

# original_queue_size: 1. rotten queue: [[2, 1]]
# cell[2, 1] = 2. queue: []. fresh: 1
# neighbor[2, 2] = 1
# ** [2, 2] turns rotten **
# neighbor[2, 0] = 0
# neighbor[1, 1] = 2
# depth: 4
# [2, 2, 2]
# [2, 2, 0]
# [0, 2, 2]

# original_queue_size: 1. rotten queue: [[2, 2]]
# cell[2, 2] = 2. queue: []. fresh: 0
# neighbor[2, 1] = 2
# neighbor[1, 2] = 0
#-----------
# original_queue_size: 1. rotten queue: [[0, 0]]
# cell[0, 0] = 2. queue: []. fresh: 6
# neighbor[0, 1] = 1
# ** [0, 1] turns rotten **
# neighbor[1, 0] = 0
# depth: 1
# [2, 2, 1]
# [0, 1, 1]
# [1, 0, 1]

# original_queue_size: 1. rotten queue: [[0, 1]]
# cell[0, 1] = 2. queue: []. fresh: 5
# neighbor[0, 2] = 1
# ** [0, 2] turns rotten **
# neighbor[0, 0] = 2
# neighbor[1, 1] = 1
# ** [1, 1] turns rotten **
# depth: 2
# [2, 2, 2]
# [0, 2, 1]
# [1, 0, 1]

# original_queue_size: 2. rotten queue: [[0, 2], [1, 1]]
# cell[0, 2] = 2. queue: [[1, 1]]. fresh: 3
# neighbor[0, 1] = 2
# neighbor[1, 2] = 1
# ** [1, 2] turns rotten **
# cell[1, 1] = 2. queue: [[1, 2]]. fresh: 2
# neighbor[1, 2] = 2
# neighbor[1, 0] = 0
# neighbor[2, 1] = 0
# neighbor[0, 1] = 2
# depth: 3
# [2, 2, 2]
# [0, 2, 2]
# [1, 0, 1]

# original_queue_size: 1. rotten queue: [[1, 2]]
# cell[1, 2] = 2. queue: []. fresh: 2
# neighbor[1, 1] = 2
# neighbor[2, 2] = 1
# ** [2, 2] turns rotten **
# neighbor[0, 2] = 2
# depth: 4
# [2, 2, 2]
# [0, 2, 2]
# [1, 0, 2]

# original_queue_size: 1. rotten queue: [[2, 2]]
# cell[2, 2] = 2. queue: []. fresh: 1
# neighbor[2, 1] = 0
# neighbor[1, 2] = 2
#-----------
# original_queue_size: 1. rotten queue: [[0, 1]]
# cell[0, 1] = 2. queue: []. fresh: 0
# neighbor[0, 0] = 0
#-----------
# original_queue_size: 2. rotten queue: [[0, 0], [0, 3]]
# cell[0, 0] = 2. queue: [[0, 3]]. fresh: 1
# neighbor[0, 1] = 1
# ** [0, 1] turns rotten **
# cell[0, 3] = 2. queue: [[0, 1]]. fresh: 0
# neighbor[0, 2] = 0
# depth: 1
# [2, 2, 0, 2]

# original_queue_size: 1. rotten queue: [[0, 1]]
# cell[0, 1] = 2. queue: []. fresh: 0
# neighbor[0, 2] = 0
# neighbor[0, 0] = 2
#-----------
# original_queue_size: 2. rotten queue: [[0, 1], [0, 4]]
# cell[0, 1] = 2. queue: [[0, 4]]. fresh: 5
# neighbor[0, 2] = 1
# ** [0, 2] turns rotten **
# neighbor[0, 0] = 1
# ** [0, 0] turns rotten **
# cell[0, 4] = 2. queue: [[0, 2], [0, 0]]. fresh: 3
# neighbor[0, 5] = 1
# ** [0, 5] turns rotten **
# neighbor[0, 3] = 1
# ** [0, 3] turns rotten **
# depth: 1
# [2, 2, 2, 2, 2, 2, 1]

# original_queue_size: 4. rotten queue: [[0, 2], [0, 0], [0, 5], [0, 3]]
# cell[0, 2] = 2. queue: [[0, 0], [0, 5], [0, 3]]. fresh: 1
# neighbor[0, 3] = 2
# neighbor[0, 1] = 2
# cell[0, 0] = 2. queue: [[0, 5], [0, 3]]. fresh: 1
# neighbor[0, 1] = 2
# cell[0, 5] = 2. queue: [[0, 3]]. fresh: 1
# neighbor[0, 6] = 1
# ** [0, 6] turns rotten **
# neighbor[0, 4] = 2
# cell[0, 3] = 2. queue: [[0, 6]]. fresh: 0
# neighbor[0, 4] = 2
# neighbor[0, 2] = 2
# depth: 2
# [2, 2, 2, 2, 2, 2, 2]

# original_queue_size: 1. rotten queue: [[0, 6]]
# cell[0, 6] = 2. queue: []. fresh: 0
# neighbor[0, 5] = 2
