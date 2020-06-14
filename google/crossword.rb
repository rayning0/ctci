# Given a nxn crossword puzzle and a word, return earliest [row, col] where you can fit that word. Fill in word right or down. Part of word may be filled in already. Length of space must exactly equal length of word.
# word = "tent"

# A _ # T _ N S # _ #
_ # T _ _ T # _ _ _ # col = [1, 2]
_ # _ _ #  # # _ # _
_ # _ _ #  # # _ # _
_ # S _ #  # # _ # _
# ...
# row, col = 1

#  _ _ _ _

# Strategy:
# 1. Solve this for 1 row only. Solve for horizontally only.
# 2. Transpose the matrix. Then we can use same code on transposed matrix to solve it vertically.

# Solve for 1 row:
# Test cases: Word = "test"
# OK. All same length as word
# 1. _ _ _ _ All blanks. Left and right of word must be either "#" or border.
# 2. T _ N _ >=1 of characters are in word

# Not OK:
# 1. _ _ T E S T _ _ Can't start word from middle
# 2. T _ _ S Can't have 1 or more letters not matching letters in word
# 3. Can't have "#" in word
# 4. T E S T _ W #

def crossword(arr, word)
  earliest_col = -1
  ans = []
  arr.each_with_index do |row, i|
    earliest_col = solve_horiz(row, word)
    ans = [i, earliest_col]
    break
  end

  tarr = transpose arr
  tarr.each_with_index do |col, i|
    earliest_row = solve_horiz(row, word)
    if earliest_row <= ans[0] && i <= ans[1]
      ans = [earliest_row, i]
    end
    break
  end

  ans
end

def solve_horiz(row, word)
  return [-1, -1] if word.size > row.size

  row.size.times do |col|
    if col == 0 && row[0] == '_' || row[0] == word[0]
      (0..word.size - 1).each do |i|
        next if row[i] == word[i]
      end
      return col if word.size < row.size && row[word.size] == '#'
      return col
    elsif row[col] == '#' && col + 1 < row.size && (row[col + 1] == word[0] || row[col + 1] == '_')
      while col + 1 < row.size do
        next if row[col + 1] == word[i - col] || row[i + 1] == '_'
        col += 1
      end
    end
  end
end

def transpose(arr)
  arr = [[4, -5, 2], [-3, 8, 10], [2, -4, 6]]
  p arr.transpose
end

p transpose(arr)
