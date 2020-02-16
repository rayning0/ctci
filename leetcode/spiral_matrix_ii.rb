# https://leetcode.com/problems/spiral-matrix-ii/
def ppp(arr)
  arr.each do |r|
    puts r.each { |p| p }.join(" ")
  end
end

def spiral_matrix(n)
  @matrix = Array.new(n){ |cell| Array.new(n, 0) }
  @matrix[0][0] = 0
  row, col, val = 0, 0, 0

  while val < n * n
    row, col, val = right(row, col)
    puts "row: #{row}, col: #{col}"
    break if val == n * n
    row, col, val = down(row, col)
    puts "row: #{row}, col: #{col}"
    break if val == n * n
    row, col, val = left(row, col)
    puts "row: #{row}, col: #{col}"
    break if val == n * n
    row, col, val = up(row, col)
    puts "row: #{row}, col: #{col}"
    break if val == n * n
  end

  @matrix
end

def right(row, col)
  val = @matrix[row][col]
  @matrix[0].size.times do |c|
    break if @matrix[row][c] != 0
    val += 1
    @matrix[row][c] = val
  end
  ppp(@matrix)

  [row, @matrix[0].size - 1, val]
end

def left(row, col)
  val = @matrix[row][col]
  endcol = 0

   col.downto(0).each do |c|
    next if @matrix[row][c] != 0
    if @matrix[row][c] != 0
      endcol = c + 1
      break
    end
    val += 1
    @matrix[row][c] = val
  end
  ppp(@matrix)

  [row, endcol, val]
end

def down(row, col)
  val = @matrix[row][col]
  @matrix.size.times do |r|
    next if @matrix[r][col] != 0
    break if @matrix[r][col] != 0
    val += 1
    @matrix[r][col] = val
  end

  ppp(@matrix)

  [@matrix.size - 1, col, val]
end

def up(row, col)
  endrow = 0
  val = @matrix[row][col]
  row.downto(0).each do |r|
    next if @matrix[r][col] != 0
    if @matrix[r][col] != 0
      endrow = r + 1
      break
    end
    val += 1
    @matrix[r][col] = val
  end

  ppp(@matrix)
  puts "*****val: #{val}"
  [endrow, col, val]
end

p spiral_matrix(3)


