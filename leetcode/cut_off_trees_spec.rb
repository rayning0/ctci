# https://leetcode.com/problems/cut-off-trees-for-golf-event/
# @param {Integer[][]} forest
# @return {Integer}
class Tree
  attr_accessor :f, :visited, :steps, :trees_cut

  def initialize(forest)
    @f = forest
    @steps = 0
    @visited = Array.new(forest.size) { |cell| Array.new(forest[0].size, '-') }
  end

  def print_grid(array)
    puts array.map { |row| row.join('       ') }
    puts
  end

  def cut
    row, col = 0, 0
    rowend = f.size - 1
    colend = f[0].size - 1
    nopath = false
    total_trees = num_trees(f)
    puts "total trees: #{total_trees}"
    @visited[0][0] = '+'
    if f[0][0] > 1
      @trees_cut = 1
      @f[0][0] = 1
    else
      @trees_cut = 0
    end

    while trees_cut < total_trees do
      steps_old = steps
      print_grid(visited)
      puts "row: #{row}, col: #{col}"
      puts "steps: #{steps}, trees_cut: #{trees_cut}"

      col += 1
      if col.between?(0, colend) && visited[row][col] == '-' && f[row][col] > 0
        step_forward(row, col)
      else
        col -= 1
      end

      row += 1
      if row.between?(0, rowend) && visited[row][col] == '-' && f[row][col] > 0
        step_forward(row, col)
      else
        row -= 1
      end

      col -= 1
      if col.between?(0, colend) && visited[row][col] == '-' && f[row][col] > 0
        step_forward(row, col)
      else
        col += 1
      end

      row -= 1
      cell = f[row][col]
      if row.between?(0, rowend) && visited[row][col] == '-' && f[row][col] > 0
        step_forward(row, col)
      else
        row += 1
      end

      if steps == steps_old
        nopath = true
        break
      end
    end

    return -1 if nopath
    puts "final steps: #{steps}"
    steps
  end

  def step_forward(row, col)
    @steps += 1
    if f[row][col] > 1  # a tree is there
      @trees_cut += 1
      @f[row][col] = 1
      print_grid(f)
    end
    @visited[row][col] = '+'
  end

  def num_trees(f)
    trees = 0
    f.each do |row|
      row.each do |cell|
        trees += 1 if cell > 1
      end
    end
    trees
  end
end

def cut_off_tree(forest)
  puts '--------------------------------'
  Tree.new(forest).cut
end

describe '#cut_off_tree' do
  context 'for 3x3 matrix' do
    it 'cuts trees clockwise' do
      forest = [
        [1,2,3],
        [0,0,4],
        [7,6,5]
      ]
      expect(cut_off_tree(forest)).to eq 6
    end

    it 'returns -1 if stuck' do
      forest = [
        [1,2,3],
        [0,0,0],
        [7,6,5]
      ]
      expect(cut_off_tree(forest)).to eq -1
    end

    it 'cuts trees clockwise, including starting cell' do
      forest = [
        [2,3,4],
        [0,0,5],
        [8,7,6]
      ]
      expect(cut_off_tree(forest)).to eq 6
    end

    it '' do
      forest = [
        [54581641,64080174,24346381,69107959],
        [86374198,61363882,68783324,79706116],
        [  668150,92178815,89819108,94701471],
        [83920491,22724204,46281641,47531096],
        [89078499,18904913,25462145,60813308]
      ]

      expect(cut_off_tree(forest)).to eq 57
    end
  end
end
