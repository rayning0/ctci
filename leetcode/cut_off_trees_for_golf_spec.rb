# https://leetcode.com/problems/cut-off-trees-for-golf-event/

def pp(arr)
  arr.each { |row| p row }
end

# BFS
def cut_off_tree(arr)
  steps = 0
  trees = count_trees(arr)
  queue = [[0, 0]]
  visited = Array.new(arr.size) { |cell| Array.new(arr[0].size, false) }

  while !queue.empty? do
    row, col = queue.shift
    next if visited[row][col]
    visited[row][col] = true
    puts "cell[#{row}, #{col}] = #{arr[row][col]}. queue: #{queue}. steps: #{steps}. trees: #{trees}"
    pp(arr)

    neighbors(row, col, arr).each do |nrow, ncol|
      puts "neighbor: [#{nrow}, #{ncol}]"
      if arr[nrow][ncol] > 1 # tree
        arr[nrow][ncol] = 1  # cut tree
        trees -= 1
        puts "** cut tree at [#{nrow}, #{ncol}] **"
      end
      queue << [nrow, ncol]
    end

    steps += 1
  end
  steps -= 1

  return -1 if trees > 0
  steps
end

def count_trees(arr)
  trees = 0
  arr.each do |row|
    row.each do |col|
      trees += 1 if col > 1
    end
  end

  trees
end

# only neighbors where we can either walk (1 = grass) or cut (> 1 = tree)
def neighbors(row, col, arr)
  height = arr.size
  width = arr[0].size
  neighbors = []
  neighbors << [row, col + 1] if col + 1 < width && arr[row][col + 1] >= 1
  neighbors << [row, col - 1] if col - 1 >= 0 && arr[row][col - 1] >= 1
  neighbors << [row + 1, col] if row + 1 < height && arr[row + 1][col] >= 1
  neighbors << [row - 1, col] if row - 1 >= 0 && arr[row - 1][col] >= 1

  neighbors
end

describe "#cut_off_trees" do
  it 'returns min # of steps to cut all trees' do
    expect(cut_off_tree([[1,2,3],[0,0,4],[7,6,5]])).to eq 6
    expect(cut_off_tree([[1,2,3],[0,0,0],[7,6,5]])).to eq -1
    expect(cut_off_tree([[2,3,4],[0,0,5],[8,7,6]])).to eq 6
  end

  it 'Does this in order of tree height, from lowest height first. We may walk past tree without cutting it.' do
    expect(cut_off_tree([
      [54581641,64080174,24346381,69107959],
      [86374198,61363882,68783324,79706116],
      [  668150,92178815,89819108,94701471],
      [83920491,22724204,46281641,47531096],
      [89078499,18904913,25462145,60813308]
    ])).to eq 57
  end
end
