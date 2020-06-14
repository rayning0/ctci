# Return array with average value of each binary tree level

class Node
  attr_accessor :left, :right, :val

  def initialize(val)
    @val = val
    @left = nil
    @right = nil
  end
end

t = Node.new(4)
t.left = Node.new(7)
t.right = Node.new(9)
t.left.left = Node.new(10)
t.right.right = Node.new(6)
t.left.right = Node.new(2)
t.left.right.right = Node.new(6)
t.left.right.right.left = Node.new(2)

#     4
#    / \
#   7   9
#  / \   \
# 10  2   6
#      \
#       6
#      /
#     2

# use BFS
def average_tree_level(t)
  return [] if t.nil?
  avgs = []
  sum = 0
  queue = [t]
  while !queue.empty? do
    level_size = queue.size
    current_level = []
    puts "level_size: #{level_size}, queue: #{queue.map{|q| q.val}}, avgs: #{avgs}"
    level_size.times do
      node = queue.shift
      current_level << node.val
      if node.left
        queue << node.left
      end
      if node.right
        queue << node.right
      end
    end
    avgs << current_level
    sum = 0
  end

  avgs
end

p average_tree_level(t)

# avgs << 4 / 1
# (7 + 9) / 2         loop 1 time
# (10 + 2 + 6) / 3    loop 2 times
# 6 / 1               loop 3 times
# 2 / 1               loop 1 time
