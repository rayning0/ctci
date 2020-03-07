# https://leetcode.com/problems/rotting-oranges/
# Runtime: 40 ms, faster than 88.17% of Ruby online submissions for Rotting Oranges.
# Memory Usage: 9.5 MB, less than 100.00% of Ruby online submissions for Rotting Oranges.

# BFS strategy:

  # depth = 0
  # queue, fresh = array of all rotten oranges, # of fresh oranges
  # While queue not empty
  #   change = false

  #   Repeat for size of original queue:
    #   Remove first cell of queue
    #   For each cell neighbor (4 directions)
        # if neighbor is fresh
        #   make neighbor rotten
        #   add neighbor to queue
        #   fresh--
        #   change = true
    # if change == true, depth++

# return depth if fresh == 0
# return -1

# Time complexity: O(n * m). Space complexity: O(n * m).
def pp(arr)
  arr.each { |row| p row }
end

def find_rotten_fresh(arr)
  rotten, fresh = [], 0
  arr.size.times do |row|
    arr[0].size.times do |col|
      rotten << [row, col] if arr[row][col] == 2
      fresh += 1 if arr[row][col] == 1
    end
  end
  [rotten, fresh]
end

def oranges(arr)
  depth = 0
  queue, fresh = find_rotten_fresh(arr) # queue has only ROTTEN tomatoes

  while !queue.empty? do
    original_queue_size = queue.size
    # puts "original_queue_size: #{original_queue_size}. rotten queue: #{queue}"
    change = false

    original_queue_size.times do
      row, col = queue.shift
      # puts "cell[#{row}, #{col}] = #{arr[row][col]}. queue: #{queue}. fresh: #{fresh}"
      neighbors(row, col, arr).each do |nrow, ncol|
        # puts "neighbor[#{nrow}, #{ncol}] = #{arr[nrow][ncol]}"
        if arr[nrow][ncol] == 1
          arr[nrow][ncol] = 2
          queue << [nrow, ncol]
          fresh -= 1
          change = true
          # puts "** [#{nrow}, #{ncol}] turns rotten **"
        end
      end
    end

    if change
      depth += 1
      # puts "depth: #{depth}"
      # pp(arr)
      # puts
    end
  end

  return depth if fresh == 0
  -1
end

def neighbors(row, col, arr)
  height, width = arr.size, arr[0].size
  neighbors = []
  neighbors << [row, col + 1] if col + 1 < width
  neighbors << [row, col - 1] if col - 1 >= 0
  neighbors << [row + 1, col] if row + 1 < height
  neighbors << [row - 1, col] if row - 1 >= 0
  neighbors
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
