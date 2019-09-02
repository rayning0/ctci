# procedure BFS(G,start_v):
#     let Q be a queue
#     label start_v as discovered
#     Q.enqueue(start_v)
#     while Q is not empty
#         v = Q.dequeue()
#         if v is the goal:
#             return v
#         for all edges from v to w in G.adjacentEdges(v) do
#             if w is not labeled as discovered:
#                 label w as discovered
#                 w.parent = v
#                 Q.enqueue(w)

def run
  a = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
  ]

  @height = a.length
  @width = a.first.length
  visited = Array.new(@height) { Array.new(@width) }

  starting_node = [0, 0]
  queue = [] # element of 2D array we're currently evaluating
  queue << starting_node
  river_length = 0
  got_zero = false
  rivers = []

  while queue.any?
    current_node = queue.shift

    node_and_adjacents(current_node).each do |adjacent_node|
      next if adjacent_node.nil?
      x, y = adjacent_node.first, adjacent_node.last
      next if visited[x][y]
      puts "node: #{adjacent_node}"

      puts "a[#{x}][#{y}] = #{a[x][y]}"
      if a[x][y] == 1
        river_length += 1
        got_zero = false
      else
        if got_zero == true && river_length > 0 # river has ende
          rivers << river_length
          got_zero = false
          river_length = 0
          binding.pry
        else
          got_zero = true
        end
      end

      queue << adjacent_node
      visited[adjacent_node.first][adjacent_node.last] = true
    end
  end
  puts "river_length: #{river_length}"
end

# returns all adjacent nodes if in bounds
def node_and_adjacents(node)
  x = node.first
  y = node.last

  right = x + 1 > @width - 1 ? nil : [x + 1, y]
  # left = x - 1 < 0 ? nil : [x - 1, y]
  down_value = y + 1 > @height - 1 ? nil : [x, y + 1]
  # up_value = y - 1 < 0 ? nil : [x, y - 1]

  # [node, left, right, up_value, down_value]
  [node, right, down_value]
end

run
