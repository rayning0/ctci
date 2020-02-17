# https://leetcode.com/problems/spiral-matrix-ii/
def print_matrix(arr)
  arr.each do |r|
    puts r.each { |p| p }.join(" ")
  end
end

def spiral_matrix(n)
  matrix = Array.new(n){ |cell| Array.new(n, 0) }
  count = 1
  col_start, col_end = 0, n - 1
  row_start, row_end = 0, n - 1

  while col_start <= col_end && row_start <= row_end do

    # right
    (col_start..col_end).each do |col|
      # puts "row_start: #{row_start}, col: #{col}"
      matrix[row_start][col] = count
      count += 1
    end
    row_start += 1

    # down
    (row_start..row_end).each do |row|
      # puts "row: #{row}, col_end: #{col_end}"
      matrix[row][col_end] = count
      count += 1
    end
    col_end -= 1

    # left
    col_end.downto(col_start).each do |col|
      # puts "row_end: #{row_end}, col: #{col}"
      matrix[row_end][col] = count
      count += 1
    end
    row_end -= 1

    # up
    row_end.downto(row_start).each do |row|
      # puts "row: #{row}, col_start: #{col_start}"
      matrix[row][col_start] = count
      count += 1
    end
    col_start += 1
  end

  matrix
end

describe '#spiral_matrix' do
  it 'creates 2x2 spiral matrix' do
    expect(spiral_matrix(2)).to eq [[1, 2],
                                    [4, 3]]
  end

  it 'creates 3x3 spiral matrix' do
    expect(spiral_matrix(3)).to eq [[1, 2, 3],
                                    [8, 9, 4],
                                    [7, 6, 5]]
  end

  it 'creates 4x4 spiral matrix' do
    expect(spiral_matrix(4)).to eq [[ 1, 2, 3, 4],
                                    [12,13,14, 5],
                                    [11,16,15, 6],
                                    [10, 9, 8, 7]]
  end
end
