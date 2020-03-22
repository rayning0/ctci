# Q: Given a nxn matrix of integers, find max sum of integers you can get by
# taking path from upper left (0, 0) to bottom right, where you can only move to right or down.

#  4  -5   2
# -3   8  10
#  2  -4   6

#  1. Use BFS. Make 2nd nxn matrix filled with -infinity to track sums.
#  2. While row, col != [n - 1, n - 1], loop
#  3. Move right or down, with boundary checking get_neighbors(). Fill in sum matrix as we go with max sum we can get at that cell so far.
#  4. When have conflict, like (4 - 5 + 8) vs (4 - 3 + 8), take max and stick in sums matrix. Memoization.

arr = [[4, -5, 2], [-3, 8, 10], [2, -4, 6]]

# queue = [[1, 1]]
# row, col = 2, 0

# nrow, ncol = 2, 1
#                                             FROM           TO
# [current value of sums[nrow, ncol], sums[row, col] + arr[nrow][ncol]].max
# sums = [7, 1 + 8].max = 9
# 4 -1  0
# 1  9  0
# 0  0  0

# Time: O(n * n), Space: O(n * n)
def max_sum_path(arr)
  queue = [[0, 0]]
  n = arr.size
  sums = Array.new(n) { |cell| Array.new(n, -100) }
  sums[0][0] = arr[0][0]

  while !queue.empty? do
    row, col = queue.shift
    directions = [[0, 1], [1, 0]]
    directions.each do |drow, dcol|
      nrow, ncol = row + drow, col + dcol
      if nrow.between?(0, n - 1) && ncol.between?(0, n - 1)
        sums[nrow][ncol] = [sums[nrow][ncol], sums[row][col] + arr[nrow][ncol]].max
        queue << [nrow, ncol]
      end
    end
  end
  sums[n - 1][n - 1]
end

p max_sum_path(arr)
