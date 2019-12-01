require 'pp'

col_rem = [[], [], [], [], [], [], [], [], []]
block_rem = [[[], [], []], [[], [], []], [[], [], []]]
a = [["5","3",".",".","7",".",".",".","."],
     ["6",".",".","1","9","5",".",".","."],
     [".","9","8",".",".",".",".","6","."],
     ["8",".",".",".","6",".",".",".","3"],
     ["4",".",".","8",".","3",".",".","1"],
     ["7",".",".",".","2",".",".",".","6"],
     [".","6",".",".",".",".","2","8","."],
     [".",".",".","4","1","9",".",".","5"],
     [".",".",".",".","8",".",".","7","9"]]


def col_diff(a)
  col_rem = [[], [], [], [], [], [], [], [], []]
  9.times do |col|
    nine = (1..9).map(&:to_s)
    9.times do |row|
      val = a[row][col]
      if nine.include?(val) || val != '.'
        nine.delete(val)
        col_rem[row][col] = '.'
      else
        col_rem[row][col] = nine.shift
      end
    end
  end
  pp col_rem
  col_rem
end

def row_diff(a)
  row_rem = [[], [], [], [], [], [], [], [], []]
  9.times do |row|
    nine = (1..9).map(&:to_s)
    9.times do |col|
      val = a[row][col]
      if nine.include?(val) || val != '.'
        nine.delete(val)
        row_rem[row][col] = '.'
      else
        row_rem[row][col] = nine.shift
      end
    end
  end
  pp row_rem
  row_rem
end

describe '#col_diff' do
  it 'return array of numbers not in row' do
    expect(row_diff(a)[1]).to eq %w(. . 1 2 . 4 6 8 9)
  end
end