# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# @param {Integer[][]} matrix
# @return {Integer}
def longest_increasing_path(matrix)
    maxlength = 0
    return 0 if matrix.empty? || matrix[0].empty?
    @height, @width = matrix.size, matrix[0].size
    lengths = Array.new(@height) {|cell| Array.new(@width, 0)}

    @height.times do |row|
        @width.times do |col|
            length = dfs(row, col, matrix, lengths)
            maxlength = [maxlength, length].max
            # puts "overall maxlength #{maxlength}"
        end
    end

    maxlength
end

def pp(matrix)
    matrix.each do |row|
        p row
    end
end

# Depth-First Search
def dfs(row, col, matrix, lengths)
    return lengths[row][col] if lengths[row][col] > 0
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    val = matrix[row][col]
    # puts "[#{row}, #{col}]"

    directions.each do |drow, dcol|
        nrow, ncol = row + drow, col + dcol
        if ncol.between?(0, @width - 1) && nrow.between?(0, @height - 1) && matrix[nrow][ncol] > val
            lengths[row][col] = [lengths[row][col], dfs(nrow, ncol, matrix, lengths)].max
            # puts "new cell: [#{nrow}, #{ncol}]"
            # pp(lengths)
        end
    end

    lengths[row][col] += 1
    lengths[row][col]
end
