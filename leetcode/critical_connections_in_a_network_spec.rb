# https://leetcode.com/problems/critical-connections-in-a-network/
# https://www.coursera.org/lecture/algorithms-part2/connected-components-Dzl65
# https://www.youtube.com/watch?v=aZXi1unBdJA (Bridges algorithm)
# https://www.youtube.com/watch?v=V6kRqdtM_Uk (Bridges source code)

# O(V + E): vertices + edges
# Runtime: 784 ms, faster than 70.00% of Ruby online submissions for Critical Connections in a Network.
# Memory Usage: 94.9 MB, less than 100.00% of Ruby online submissions for Critical Connections in a Network.
class Graph
  attr_accessor :n, :id, :ids, :connections, :graph, :visited, :lowlink, :bridges

  def initialize(n, connections)
    @id, @n, @connections, @bridges = -1, n, connections, []
    @ids, @visited = Array.new(n, 0), Array.new(n, false)
    @lowlink = Array.new(n, 0) # smallest node reachable from current node, including itself
    @graph = Hash.new{ |hash, key| hash[key] = [] }

    # undirected graph automatically points both directions
    connections.each do |u, v|
      @graph[u] << v
      @graph[v] << u
    end

    # puts "Connections: #{connections}"
    # puts "Graph: #{graph}"
  end

  # ---depth-first search to find bridges across connected components---
  # current: node now
  # previous: node before
  # to: next node
  def dfs(current, previous)
    visited[current] = true
    @id += 1
    lowlink[current] = id
    ids[current] = id

    # puts "\ncurrent: #{current}, ids: #{ids}, lowlink: #{lowlink}"
    # puts "adjacent: #{graph[current]}, visited: #{visited}, id: #{id}"

    # for each adjacent edge from 'current' to 'to'
    graph[current].each do |to|
      # puts "to: #{to}"
      next if to == previous # don't return to previous node (for undirected graph)
      if !visited[to]
        dfs(to, current)

        # Propagate smallest node we may reach from current
        lowlink[current] = [lowlink[current], lowlink[to]].min
        # puts "lowlink: #{lowlink}. lowlink[#{current}]: #{lowlink[current]}"

        # If no way to drop from 'to' node to current node #,
        # there's no path back to current node. Thus we found a BRIDGE!
        if ids[current] < lowlink[to]
          bridges << [current, to]
          # puts "------>> bridges: #{bridges} <<------- ids[#{current}] (#{ids[current]}) < lowlink[#{to}] (#{lowlink[to]})"
        end
      else
        # puts "** visited all adjacent nodes. drop lowlink[current] if lowlink[#{to}] (#{lowlink[to]}) < lowlink[#{current}] (#{lowlink[current]}) **"
        lowlink[current] = [lowlink[current], lowlink[to]].min
        # puts "lowlink: #{lowlink}. lowlink[#{current}]: #{lowlink[current]}"
      end
    end

    bridges
  end
end

def critical_connections(n, connections)
  # puts "----------------------------------------------\n\n"
  Graph.new(n, connections).dfs(0, -1)
end

describe "it gives all critical connections in the network" do
  it 'if 1 edge sticks out' do
    expect(critical_connections(4, [[0,1],[1,2],[2,0],[1,3]])).to eq [[1, 3]]
  end

  it 'if 1 edge links 2 triangles' do
    expect(critical_connections(6, [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]])).to eq [[1, 3]]
  end

  it 'if each vertex is connected to all other vertices, except 1' do
    expect(critical_connections(5, [[1,0],[2,0],[3,2],[4,2],[4,3],[3,0],[4,0]])).to eq [[0, 1]]
  end
end

# Same code with no comments:

# def dfs(current, previous)
#   visited[current] = true
#   @id += 1
#   lowlink[current] = id
#   ids[current] = id

#   graph[current].each do |to|
#     next if to == previous
#     if !visited[to]
#       dfs(to, current)
#       lowlink[current] = [lowlink[current], lowlink[to]].min

#       if ids[current] < lowlink[to]
#         bridges << [current, to]
#       end
#     else
#       lowlink[current] = [lowlink[current], lowlink[to]].min
#     end
#   end

#   bridges
# end

# Connections: [[0, 1], [1, 2], [2, 0], [1, 3]]
# Graph: {0=>[1, 2], 1=>[0, 2, 3], 2=>[1, 0], 3=>[1]}

# current: 0, ids: [0, 0, 0, 0], lowlink: [0, 0, 0, 0]
# adjacent: [1, 2], visited: [true, false, false, false], id: 0
# to: 1

# current: 1, ids: [0, 1, 0, 0], lowlink: [0, 1, 0, 0]
# adjacent: [0, 2, 3], visited: [true, true, false, false], id: 1
# to: 0
# to: 2

# current: 2, ids: [0, 1, 2, 0], lowlink: [0, 1, 2, 0]
# adjacent: [1, 0], visited: [true, true, true, false], id: 2
# to: 1
# to: 0
# ** visited all adjacent nodes. drop lowlink[current] if lowlink[0] (0) < lowlink[2] (2) **
# lowlink: [0, 1, 0, 0]. lowlink[2]: 0
# lowlink: [0, 0, 0, 0]. lowlink[1]: 0
# to: 3

# current: 3, ids: [0, 1, 2, 3], lowlink: [0, 0, 0, 3]
# adjacent: [1], visited: [true, true, true, true], id: 3
# to: 1
# lowlink: [0, 0, 0, 3]. lowlink[1]: 0
# ------>> bridges: [[1, 3]] <<------- ids[1] (1) < lowlink[3] (3)
# lowlink: [0, 0, 0, 3]. lowlink[0]: 0
# to: 2
# ** visited all adjacent nodes. drop lowlink[current] if lowlink[2] (0) < lowlink[0] (0) **
# lowlink: [0, 0, 0, 3]. lowlink[0]: 0

# ----------------------------------------------

# Connections: [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3]]
# Graph: {0=>[1, 2], 1=>[0, 2, 3], 2=>[1, 0], 3=>[1, 4, 5], 4=>[3, 5], 5=>[4, 3]}

# current: 0, ids: [0, 0, 0, 0, 0, 0], lowlink: [0, 0, 0, 0, 0, 0]
# adjacent: [1, 2], visited: [true, false, false, false, false, false], id: 0
# to: 1

# current: 1, ids: [0, 1, 0, 0, 0, 0], lowlink: [0, 1, 0, 0, 0, 0]
# adjacent: [0, 2, 3], visited: [true, true, false, false, false, false], id: 1
# to: 0
# to: 2

# current: 2, ids: [0, 1, 2, 0, 0, 0], lowlink: [0, 1, 2, 0, 0, 0]
# adjacent: [1, 0], visited: [true, true, true, false, false, false], id: 2
# to: 1
# to: 0
# ** visited all adjacent nodes. drop lowlink[current] if lowlink[0] (0) < lowlink[2] (2) **
# lowlink: [0, 1, 0, 0, 0, 0]. lowlink[2]: 0
# lowlink: [0, 0, 0, 0, 0, 0]. lowlink[1]: 0
# to: 3

# current: 3, ids: [0, 1, 2, 3, 0, 0], lowlink: [0, 0, 0, 3, 0, 0]
# adjacent: [1, 4, 5], visited: [true, true, true, true, false, false], id: 3
# to: 1
# to: 4

# current: 4, ids: [0, 1, 2, 3, 4, 0], lowlink: [0, 0, 0, 3, 4, 0]
# adjacent: [3, 5], visited: [true, true, true, true, true, false], id: 4
# to: 3
# to: 5

# current: 5, ids: [0, 1, 2, 3, 4, 5], lowlink: [0, 0, 0, 3, 4, 5]
# adjacent: [4, 3], visited: [true, true, true, true, true, true], id: 5
# to: 4
# to: 3
# ** visited all adjacent nodes. drop lowlink[current] if lowlink[3] (3) < lowlink[5] (5) **
# lowlink: [0, 0, 0, 3, 4, 3]. lowlink[5]: 3
# lowlink: [0, 0, 0, 3, 3, 3]. lowlink[4]: 3
# lowlink: [0, 0, 0, 3, 3, 3]. lowlink[3]: 3
# to: 5
# ** visited all adjacent nodes. drop lowlink[current] if lowlink[5] (3) < lowlink[3] (3) **
# lowlink: [0, 0, 0, 3, 3, 3]. lowlink[3]: 3
# lowlink: [0, 0, 0, 3, 3, 3]. lowlink[1]: 0
# ------>> bridges: [[1, 3]] <<------- ids[1] (1) < lowlink[3] (3)
# lowlink: [0, 0, 0, 3, 3, 3]. lowlink[0]: 0
# to: 2
# ** visited all adjacent nodes. drop lowlink[current] if lowlink[2] (0) < lowlink[0] (0) **
# lowlink: [0, 0, 0, 3, 3, 3]. lowlink[0]: 0

# ----------------------------------------------

# Connections: [[1, 0], [2, 0], [3, 2], [4, 2], [4, 3], [3, 0], [4, 0]]
# Graph: {1=>[0], 0=>[1, 2, 3, 4], 2=>[0, 3, 4], 3=>[2, 4, 0], 4=>[2, 3, 0]}

# current: 0, ids: [0, 0, 0, 0, 0], lowlink: [0, 0, 0, 0, 0]
# adjacent: [1, 2, 3, 4], visited: [true, false, false, false, false], id: 0
# to: 1

# current: 1, ids: [0, 1, 0, 0, 0], lowlink: [0, 1, 0, 0, 0]
# adjacent: [0], visited: [true, true, false, false, false], id: 1
# to: 0
# lowlink: [0, 1, 0, 0, 0]. lowlink[0]: 0
# ------>> bridges: [[0, 1]] <<------- ids[0] (0) < lowlink[1] (1)
# to: 2

# current: 2, ids: [0, 1, 2, 0, 0], lowlink: [0, 1, 2, 0, 0]
# adjacent: [0, 3, 4], visited: [true, true, true, false, false], id: 2
# to: 0
# to: 3

# current: 3, ids: [0, 1, 2, 3, 0], lowlink: [0, 1, 2, 3, 0]
# adjacent: [2, 4, 0], visited: [true, true, true, true, false], id: 3
# to: 2
# to: 4

# current: 4, ids: [0, 1, 2, 3, 4], lowlink: [0, 1, 2, 3, 4]
# adjacent: [2, 3, 0], visited: [true, true, true, true, true], id: 4
# to: 2
# ** visited all adjacent nodes. drop lowlink[current] if lowlink[2] (2) < lowlink[4] (4) **
# lowlink: [0, 1, 2, 3, 2]. lowlink[4]: 2
# to: 3
# to: 0
# ** visited all adjacent nodes. drop lowlink[current] if lowlink[0] (0) < lowlink[4] (2) **
# lowlink: [0, 1, 2, 3, 0]. lowlink[4]: 0
# lowlink: [0, 1, 2, 0, 0]. lowlink[3]: 0
# to: 0
# ** visited all adjacent nodes. drop lowlink[current] if lowlink[0] (0) < lowlink[3] (0) **
# lowlink: [0, 1, 2, 0, 0]. lowlink[3]: 0
# lowlink: [0, 1, 0, 0, 0]. lowlink[2]: 0
# to: 4
# ** visited all adjacent nodes. drop lowlink[current] if lowlink[4] (0) < lowlink[2] (0) **
# lowlink: [0, 1, 0, 0, 0]. lowlink[2]: 0
# lowlink: [0, 1, 0, 0, 0]. lowlink[0]: 0
# to: 3
# ** visited all adjacent nodes. drop lowlink[current] if lowlink[3] (0) < lowlink[0] (0) **
# lowlink: [0, 1, 0, 0, 0]. lowlink[0]: 0
# to: 4
# ** visited all adjacent nodes. drop lowlink[current] if lowlink[4] (0) < lowlink[0] (0) **
# lowlink: [0, 1, 0, 0, 0]. lowlink[0]: 0
