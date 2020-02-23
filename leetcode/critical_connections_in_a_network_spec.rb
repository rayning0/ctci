# https://leetcode.com/problems/critical-connections-in-a-network/
# https://www.youtube.com/watch?v=aZXi1unBdJA (Bridges algorithm)
# https://www.youtube.com/watch?v=V6kRqdtM_Uk (Bridges source code)
# This test fails: https://leetcode.com/submissions/detail/305923798/testcase/
# O(V + E): vertices + edges
class Graph
  attr_accessor :n, :id, :connections, :alist, :visited, :lowlink, :bridges

  def initialize(n, connections)
    @connections = connections
    @n = n # number of nodes
    puts "Starting Connections: #{connections}"

    # Adjacency List view of a graph
    # https://www.geeksforgeeks.org/graph-and-its-representations/
    @alist = adjacency_list
    puts "Starting Adjacency List: #{alist}"

    @lowlink = Array.new(n, 0) # smallest node reachable from current node, including itself
    @visited = Array.new(n, false)
    @id = 0
  end

  # find all bridges in graph across connected components
  def find_bridges
    @bridges = []
    n.times do |node|
      puts "node: #{node}, bridges: #{bridges}"
      dfs(node, -1) if !visited[node]
    end

    puts "\nlowlink: #{lowlink}"
    puts "-----------------------\n\n"
    bridges
  end

  # ---depth-first search to find bridges---
  # current: node now
  # previous: node before
  # to: next node
  def dfs(current, previous)
    visited[current] = true
    @id += 1
    lowlink[current] = id
    puts "current: #{current}, adjacent: #{alist[current]}, lowlink: #{lowlink}, visited: #{visited}, id: #{id}"

    # for each adjacent edge from 'current' to 'to'
    alist[current].each do |to|
      puts "to: #{to}"
      next if to == previous # don't return to previous node (for undirected graph)
      if !visited[to]
        dfs(to, current)

        # track smallest node we may reach from current
        lowlink[current] = [lowlink[current], lowlink[to]].min
        puts "lowlink[#{current}]: #{lowlink[current]}"

        # If no way to drop from 'to' node to current node #, it means
        # there's no path back to current node. Thus we found a BRIDGE!
        if current < lowlink[to]
          bridges << [current, to]
          puts "bridges: #{bridges}. current = #{current} < lowlink[to = #{to}] = #{lowlink[to]}"
        end
      else
        puts "** visited all adjacent nodes. drop lowlink[current]: #{lowlink[current]} if 'to' = #{to} < lowlink[#{current}] = #{lowlink[current]} **"
        lowlink[current] = [lowlink[current], to].min
        puts "lowlink[#{current}]: #{lowlink[current]}"
      end
    end
  end

  def adjacency_list
    alist = {}
    connections.each do |a, b|
      alist[a] ? alist[a] << b : alist[a] = [b]
      alist[b] ? alist[b] << a : alist[b] = [a]
    end

    alist
  end
end

def critical_connections(n, connections)
  Graph.new(n, connections).find_bridges
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

# Starting Connections: [[0, 1], [1, 2], [2, 0], [1, 3]]
# Starting Adjacency List: {0=>[1, 2], 1=>[0, 2, 3], 2=>[1, 0], 3=>[1]}
# node: 0, bridges: []
# current: 0, adjacent: [1, 2], lowlink: [1, 0, 0, 0], visited: [true, false, false, false], id: 1
# to: 1
# current: 1, adjacent: [0, 2, 3], lowlink: [1, 2, 0, 0], visited: [true, true, false, false], id: 2
# to: 0
# to: 2
# current: 2, adjacent: [1, 0], lowlink: [1, 2, 3, 0], visited: [true, true, true, false], id: 3
# to: 1
# to: 0
# ** visited all adjacent nodes. drop lowlink[current]: 3 if 'to' = 0 < lowlink[2] = 3 **
# lowlink[2]: 0
# lowlink[1]: 0
# to: 3
# current: 3, adjacent: [1], lowlink: [1, 0, 0, 4], visited: [true, true, true, true], id: 4
# to: 1
# lowlink[1]: 0
# bridges: [[1, 3]]. current = 1 < lowlink[to = 3] = 4
# lowlink[0]: 0
# to: 2
# ** visited all adjacent nodes. drop lowlink[current]: 0 if 'to' = 2 < lowlink[0] = 0 **
# lowlink[0]: 0
# node: 1, bridges: [[1, 3]]
# node: 2, bridges: [[1, 3]]
# node: 3, bridges: [[1, 3]]

# lowlink: [0, 0, 0, 4]
# -----------------------

# Starting Connections: [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3]]
# Starting Adjacency List: {0=>[1, 2], 1=>[0, 2, 3], 2=>[1, 0], 3=>[1, 4, 5], 4=>[3, 5], 5=>[4, 3]}
# node: 0, bridges: []
# current: 0, adjacent: [1, 2], lowlink: [1, 0, 0, 0, 0, 0], visited: [true, false, false, false, false, false], id: 1
# to: 1
# current: 1, adjacent: [0, 2, 3], lowlink: [1, 2, 0, 0, 0, 0], visited: [true, true, false, false, false, false], id: 2
# to: 0
# to: 2
# current: 2, adjacent: [1, 0], lowlink: [1, 2, 3, 0, 0, 0], visited: [true, true, true, false, false, false], id: 3
# to: 1
# to: 0
# ** visited all adjacent nodes. drop lowlink[current]: 3 if 'to' = 0 < lowlink[2] = 3 **
# lowlink[2]: 0
# lowlink[1]: 0
# to: 3
# current: 3, adjacent: [1, 4, 5], lowlink: [1, 0, 0, 4, 0, 0], visited: [true, true, true, true, false, false], id: 4
# to: 1
# to: 4
# current: 4, adjacent: [3, 5], lowlink: [1, 0, 0, 4, 5, 0], visited: [true, true, true, true, true, false], id: 5
# to: 3
# to: 5
# current: 5, adjacent: [4, 3], lowlink: [1, 0, 0, 4, 5, 6], visited: [true, true, true, true, true, true], id: 6
# to: 4
# to: 3
# ** visited all adjacent nodes. drop lowlink[current]: 6 if 'to' = 3 < lowlink[5] = 6 **
# lowlink[5]: 3
# lowlink[4]: 3
# lowlink[3]: 3
# to: 5
# ** visited all adjacent nodes. drop lowlink[current]: 3 if 'to' = 5 < lowlink[3] = 3 **
# lowlink[3]: 3
# lowlink[1]: 0
# bridges: [[1, 3]]. current = 1 < lowlink[to = 3] = 3
# lowlink[0]: 0
# to: 2
# ** visited all adjacent nodes. drop lowlink[current]: 0 if 'to' = 2 < lowlink[0] = 0 **
# lowlink[0]: 0
# node: 1, bridges: [[1, 3]]
# node: 2, bridges: [[1, 3]]
# node: 3, bridges: [[1, 3]]
# node: 4, bridges: [[1, 3]]
# node: 5, bridges: [[1, 3]]

# lowlink: [0, 0, 0, 3, 3, 3]
# -----------------------

# Starting Connections: [[1, 0], [2, 0], [3, 2], [4, 2], [4, 3], [3, 0], [4, 0]]
# Starting Adjacency List: {1=>[0], 0=>[1, 2, 3, 4], 2=>[0, 3, 4], 3=>[2, 4, 0], 4=>[2, 3, 0]}
# node: 0, bridges: []
# current: 0, adjacent: [1, 2, 3, 4], lowlink: [1, 0, 0, 0, 0], visited: [true, false, false, false, false], id: 1
# to: 1
# current: 1, adjacent: [0], lowlink: [1, 2, 0, 0, 0], visited: [true, true, false, false, false], id: 2
# to: 0
# lowlink[0]: 1
# bridges: [[0, 1]]. current = 0 < lowlink[to = 1] = 2
# to: 2
# current: 2, adjacent: [0, 3, 4], lowlink: [1, 2, 3, 0, 0], visited: [true, true, true, false, false], id: 3
# to: 0
# to: 3
# current: 3, adjacent: [2, 4, 0], lowlink: [1, 2, 3, 4, 0], visited: [true, true, true, true, false], id: 4
# to: 2
# to: 4
# current: 4, adjacent: [2, 3, 0], lowlink: [1, 2, 3, 4, 5], visited: [true, true, true, true, true], id: 5
# to: 2
# ** visited all adjacent nodes. drop lowlink[current]: 5 if 'to' = 2 < lowlink[4] = 5 **
# lowlink[4]: 2
# to: 3
# to: 0
# ** visited all adjacent nodes. drop lowlink[current]: 2 if 'to' = 0 < lowlink[4] = 2 **
# lowlink[4]: 0
# lowlink[3]: 0
# to: 0
# ** visited all adjacent nodes. drop lowlink[current]: 0 if 'to' = 0 < lowlink[3] = 0 **
# lowlink[3]: 0
# lowlink[2]: 0
# to: 4
# ** visited all adjacent nodes. drop lowlink[current]: 0 if 'to' = 4 < lowlink[2] = 0 **
# lowlink[2]: 0
# lowlink[0]: 0
# to: 3
# ** visited all adjacent nodes. drop lowlink[current]: 0 if 'to' = 3 < lowlink[0] = 0 **
# lowlink[0]: 0
# to: 4
# ** visited all adjacent nodes. drop lowlink[current]: 0 if 'to' = 4 < lowlink[0] = 0 **
# lowlink[0]: 0
# node: 1, bridges: [[0, 1]]
# node: 2, bridges: [[0, 1]]
# node: 3, bridges: [[0, 1]]
# node: 4, bridges: [[0, 1]]

# lowlink: [0, 2, 0, 0, 0]
