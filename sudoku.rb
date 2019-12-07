# Sudoku Solver: https://leetcode.com/problems/sudoku-solver/.
# Good video solution guide (Python): https://www.youtube.com/watch?v=lK4N8E6uNr4
# STRATEGY:
# 1. Write find_empty(a), to find next empty cell in board a.
# 2. Write valid?(a, num, row, col), to return T/F if num is valid choice at [row, col].
# Check 3 ways: horizontally, vertically, and in the right 3x3 box of [row, col].

# 3. Recursive answer sudoku(a):
#   a. Find row, col of next empty cell. If it's [nil, nil], return T. We're done!
#   b. Loop num from 1 to 9 (all possible values):
#      i. If num is valid at [row, col] of next empty cell:
#          - set empty cell to num
#          - return T if no more empty cells
#
#          If either of 2 things happen, we BACKTRACK (https://www.javatpoint.com/backtracking-introduction):
#          1. Run out of numbers (1-9) to fill the cell
#          2. Board runs out of empty cells for the num we're trying
#          See comments below for what BACKTRACKING means.
require 'pp'

a = [["5","3",".",".","7",".",".",".","."],
     ["6",".",".","1","9","5",".",".","."],
     [".","9","8",".",".",".",".","6","."],
     ["8",".",".",".","6",".",".",".","3"],
     ["4",".",".","8",".","3",".",".","1"],
     ["7",".",".",".","2",".",".",".","6"],
     [".","6",".",".",".",".","2","8","."],
     [".",".",".","4","1","9",".",".","5"],
     [".",".",".",".","8",".",".","7","9"]]

def find_empty(a)
  a.size.times do |row|
    a[0].size.times do |col|
      return [row, col] if a[row][col] == '.'
    end
  end

  [nil, nil]
end

def valid?(a, num, row, col)
  a[row].each do |col_val|
    return false if col_val == num.to_s
  end

  a.size.times do |r|
    return false if a[r][col] == num.to_s
  end

  # If row = 0 to 2, row / 3 * 3 = 0
  # If row = 3 to 5, row / 3 * 3 = 3
  # If row = 6 to 8, row / 3 * 3 = 6
  rstart = row / 3 * 3
  cstart = col / 3 * 3

  (rstart..rstart + 2).each do |r|
    (cstart..cstart + 2).each do |c|
      return false if a[r][c] == num.to_s
    end
  end

  true
end

def sudoku(a)
  row, col = find_empty(a)
  puts "Next empty cell: [#{row}, #{col}]"
  return true if row.nil? && col.nil? # We're done!

  (1..9).each do |num|
    if valid?(a, num, row, col)
      a[row][col] = num.to_s
      puts "Put #{num} into empty cell [#{row}, #{col}]"
      return true if sudoku(a)

      # Only hits this line in 2 cases:
      # 1. We run out of numbers (1-9) to fill that cell
      # 2. Board runs out of empty cells for the num we're trying

      # If one of these is true, code will BACKTRACK:
      # - It makes cell empty again ('.')
      # - It goes up to previous recursive loop and tries next possible num (1-9)
      puts "No more numbers to try or empty cells. Backtracking...Making [#{row}, #{col}] empty again."
      a[row][col] = '.'
    end
  end

  false
end

pp a
puts '-------------------------------------'
sudoku(a)
pp a

# OUTPUT:
# [["5", "3", ".", ".", "7", ".", ".", ".", "."],
#  ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#  [".", "9", "8", ".", ".", ".", ".", "6", "."],
#  ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#  ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#  ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#  [".", "6", ".", ".", ".", ".", "2", "8", "."],
#  [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#  [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
# -------------------------------------
# [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
#  ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
#  ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
#  ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
#  ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
#  ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
#  ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
#  ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
#  ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]

# Uncommenting above print statements:
# Next empty cell: [0, 2]
# Put 1 into empty cell [0, 2]
# Next empty cell: [0, 3]
# Put 2 into empty cell [0, 3]
# Next empty cell: [0, 5]
# Put 4 into empty cell [0, 5]
# Next empty cell: [0, 6]
# Put 8 into empty cell [0, 6]
# Next empty cell: [0, 7]
# Put 9 into empty cell [0, 7]
# Next empty cell: [0, 8]
# No more numbers to try or empty cells. Backtracking...Making [0, 7] empty again.
# No more numbers to try or empty cells. Backtracking...Making [0, 6] empty again.
# Put 9 into empty cell [0, 6]
# Next empty cell: [0, 7]
# No more numbers to try or empty cells. Backtracking...Making [0, 6] empty again.
# No more numbers to try or empty cells. Backtracking...Making [0, 5] empty again.
# Put 6 into empty cell [0, 5]
# Next empty cell: [0, 6]
# Put 4 into empty cell [0, 6]
# Next empty cell: [0, 7]
# Put 9 into empty cell [0, 7]
# Next empty cell: [0, 8]
# Put 8 into empty cell [0, 8]
# Next empty cell: [1, 1]
# Put 2 into empty cell [1, 1]
# Next empty cell: [1, 2]
# Put 4 into empty cell [1, 2]
# Next empty cell: [1, 6]
# Put 3 into empty cell [1, 6]
# Next empty cell: [1, 7]
# No more numbers to try or empty cells. Backtracking...Making [1, 6] empty again.
# Put 7 into empty cell [1, 6]
# Next empty cell: [1, 7]
# Put 3 into empty cell [1, 7]
# Next empty cell: [1, 8]
# No more numbers to try or empty cells. Backtracking...Making [1, 7] empty again.
# No more numbers to try or empty cells. Backtracking...Making [1, 6] empty again.
# No more numbers to try or empty cells. Backtracking...Making [1, 2] empty again.
# Put 7 into empty cell [1, 2]
# Next empty cell: [1, 6]
# Put 3 into empty cell [1, 6]
# Next empty cell: [1, 7]
# No more numbers to try or empty cells. Backtracking...Making [1, 6] empty again.
# No more numbers to try or empty cells. Backtracking...Making [1, 2] empty again.
# No more numbers to try or empty cells. Backtracking...Making [1, 1] empty again.
# Put 4 into empty cell [1, 1]
# Next empty cell: [1, 2]
# Put 2 into empty cell [1, 2]
# Next empty cell: [1, 6]
# Put 3 into empty cell [1, 6]
# Next empty cell: [1, 7]
# No more numbers to try or empty cells. Backtracking...Making [1, 6] empty again.
# Put 7 into empty cell [1, 6]
# Next empty cell: [1, 7]
# Put 3 into empty cell [1, 7]
# Next empty cell: [1, 8]
# No more numbers to try or empty cells. Backtracking...Making [1, 7] empty again.
# No more numbers to try or empty cells. Backtracking...Making [1, 6] empty again.
# No more numbers to try or empty cells. Backtracking...Making [1, 2] empty again.
# Put 7 into empty cell [1, 2]
# Next empty cell: [1, 6]
# Put 3 into empty cell [1, 6]
# Next empty cell: [1, 7]
# Put 2 into empty cell [1, 7]
# Next empty cell: [1, 8]
# No more numbers to try or empty cells. Backtracking...Making [1, 7] empty again.
# No more numbers to try or empty cells. Backtracking...Making [1, 6] empty again.
# No more numbers to try or empty cells. Backtracking...Making [1, 2] empty again.
# No more numbers to try or empty cells. Backtracking...Making [1, 1] empty again.
# Put 7 into empty cell [1, 1]
# Next empty cell: [1, 2]
# Put 2 into empty cell [1, 2]
# Next empty cell: [1, 6]
# Put 3 into empty cell [1, 6]
# Next empty cell: [1, 7]
# No more numbers to try or empty cells. Backtracking...Making [1, 6] empty again.
# No more numbers to try or empty cells. Backtracking...Making [1, 2] empty again.
# Put 4 into empty cell [1, 2]
# Next empty cell: [1, 6]
# Put 3 into empty cell [1, 6]
# Next empty cell: [1, 7]
# Put 2 into empty cell [1, 7]
# Next empty cell: [1, 8]
# No more numbers to try or empty cells. Backtracking...Making [1, 7] empty again.
# No more numbers to try or empty cells. Backtracking...Making [1, 6] empty again.
# No more numbers to try or empty cells. Backtracking...Making [1, 2] empty again.
# No more numbers to try or empty cells. Backtracking...Making [1, 1] empty again.
# No more numbers to try or empty cells. Backtracking...Making [0, 8] empty again.
# No more numbers to try or empty cells. Backtracking...Making [0, 7] empty again.
# No more numbers to try or empty cells. Backtracking...Making [0, 6] empty again.
# Put 8 into empty cell [0, 6]
# Next empty cell: [0, 7]
# Put 4 into empty cell [0, 7]
# Next empty cell: [0, 8]
# No more numbers to try or empty cells. Backtracking...Making [0, 7] empty again.
# Put 9 into empty cell [0, 7]
# Next empty cell: [0, 8]
# Put 4 into empty cell [0, 8]
# ...etc...