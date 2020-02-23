# https://leetcode.com/problems/critical-connections-in-a-network/
# https://www.coursera.org/lecture/algorithms-part2/connected-components-Dzl65
# https://algs4.cs.princeton.edu/41graph/CC.java.html
# https://www.youtube.com/watch?v=aZXi1unBdJA (Bridges Algorithm)

# O(V + E): vertices + edges
class Graph
  attr_accessor :n, :s, :connections, :old_connections, :alist, :old_alist, :visited, :v_connections

  def initialize(n, connections)
    @connections = connections
    @old_connections = connections.dup
    @s = connections.size
    puts "Starting Connections: #{connections}"

    # Adjacency List view of a graph
    # https://www.geeksforgeeks.org/graph-and-its-representations/
    @alist = adjacency_list
    @old_alist = alist.dup
    puts "Starting Adjacency List: #{alist}"
  end

  def cc
    crit_connections = []
    start_num_of_components = component_count
    puts "Starting # of components: #{start_num_of_components}\n\n"

    s.times do |i|
      @connections = old_connections.dup
      v, w = old_connections[i]

      if old_alist[v].size == 1     # vertex only connects to 1 other
        @connections[i] = [v, v]
      elsif old_alist[w].size == 1  # vertex only connects to 1 other
        @connections[i] = [w, w]
      elsif i == 0
        @connections = connections[1..-1]
      elsif i == s - 1
        @connections = connections[0..-2]
      else
        @connections = connections[0..i - 1] + connections[i + 1..-1]
      end

      @alist = adjacency_list
      puts "Delete [#{v}, #{w}]"
      puts "New Connections: #{connections}"
      puts "New Adjacency List: #{alist}"
      cct = component_count
      puts "Component count: #{cct}\n\n"
      if cct > start_num_of_components
        crit_connections << [v, w]
      end
    end
    puts "------------------"

    crit_connections
  end

  def component_count
    @visited = Array.new(s, false)
    @v_connections = []
    count = 0

    alist.keys.each do |v|
      if visited[v] == false
        vc = dfs(v)
        puts "Connected component: #{vc}"
        @v_connections = []
        count += 1
      end
    end

    count
  end

  # return all connections to v with depth-first search
  def dfs(v)
    visited[v] = true
    v_connections << v

    alist[v].each do |w|
      dfs(w) if visited[w] == false
    end

    v_connections
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
  Graph.new(n, connections).cc
end

describe "it gives all critical connections in the network" do
  it 'if 1 edge sticks out' do
    expect(critical_connections(4, [[0,1],[1,2],[2,0],[1,3]])).to eq [[1, 3]]
  end

  it 'if 1 edge links 2 triangles' do
    expect(critical_connections(7, [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]])).to eq [[1, 3]]
  end

  it 'if each vertex is connected to all other vertices, except 1' do
    expect(critical_connections(5, [[1,0],[2,0],[3,2],[4,2],[4,3],[3,0],[4,0]])).to eq [[1, 0]]
  end
end

# Starting Connections: [[0, 1], [1, 2], [2, 0], [1, 3]]
# Starting Adjacency List: {0=>[1, 2], 1=>[0, 2, 3], 2=>[1, 0], 3=>[1]}
# Connected component: [0, 1, 2, 3]
# Starting # of components: 1

# Delete [0, 1]
# New Connections: [[1, 2], [2, 0], [1, 3]]
# New Adjacency List: {1=>[2, 3], 2=>[1, 0], 0=>[2], 3=>[1]}
# Connected component: [1, 2, 0, 3]
# Component count: 1

# Delete [1, 2]
# New Connections: [[0, 1], [2, 0], [1, 3]]
# New Adjacency List: {0=>[1, 2], 1=>[0, 3], 2=>[0], 3=>[1]}
# Connected component: [0, 1, 3, 2]
# Component count: 1

# Delete [2, 0]
# New Connections: [[0, 1], [1, 2], [1, 3]]
# New Adjacency List: {0=>[1], 1=>[0, 2, 3], 2=>[1], 3=>[1]}
# Connected component: [0, 1, 2, 3]
# Component count: 1

# Delete [1, 3]
# New Connections: [[0, 1], [1, 2], [2, 0], [3, 3]]
# New Adjacency List: {0=>[1, 2], 1=>[0, 2], 2=>[1, 0], 3=>[3, 3]}
# Connected component: [0, 1, 2]
# Connected component: [3]
# Component count: 2

# ------------------
# Starting Connections: [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3]]
# Starting Adjacency List: {0=>[1, 2], 1=>[0, 2, 3], 2=>[1, 0], 3=>[1, 4, 5], 4=>[3, 5], 5=>[4, 3]}
# Connected component: [0, 1, 2, 3, 4, 5]
# Starting # of components: 1

# Delete [0, 1]
# New Connections: [[1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3]]
# New Adjacency List: {1=>[2, 3], 2=>[1, 0], 0=>[2], 3=>[1, 4, 5], 4=>[3, 5], 5=>[4, 3]}
# Connected component: [1, 2, 0, 3, 4, 5]
# Component count: 1

# Delete [1, 2]
# New Connections: [[0, 1], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3]]
# New Adjacency List: {0=>[1, 2], 1=>[0, 3], 2=>[0], 3=>[1, 4, 5], 4=>[3, 5], 5=>[4, 3]}
# Connected component: [0, 1, 3, 4, 5, 2]
# Component count: 1

# Delete [2, 0]
# New Connections: [[0, 1], [1, 2], [1, 3], [3, 4], [4, 5], [5, 3]]
# New Adjacency List: {0=>[1], 1=>[0, 2, 3], 2=>[1], 3=>[1, 4, 5], 4=>[3, 5], 5=>[4, 3]}
# Connected component: [0, 1, 2, 3, 4, 5]
# Component count: 1

# Delete [1, 3]
# New Connections: [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 3]]
# New Adjacency List: {0=>[1, 2], 1=>[0, 2], 2=>[1, 0], 3=>[4, 5], 4=>[3, 5], 5=>[4, 3]}
# Connected component: [0, 1, 2]
# Connected component: [3, 4, 5]
# Component count: 2

# Delete [3, 4]
# New Connections: [[0, 1], [1, 2], [2, 0], [1, 3], [4, 5], [5, 3]]
# New Adjacency List: {0=>[1, 2], 1=>[0, 2, 3], 2=>[1, 0], 3=>[1, 5], 4=>[5], 5=>[4, 3]}
# Connected component: [0, 1, 2, 3, 5, 4]
# Component count: 1

# Delete [4, 5]
# New Connections: [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [5, 3]]
# New Adjacency List: {0=>[1, 2], 1=>[0, 2, 3], 2=>[1, 0], 3=>[1, 4, 5], 4=>[3], 5=>[3]}
# Connected component: [0, 1, 2, 3, 4, 5]
# Component count: 1

# Delete [5, 3]
# New Connections: [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5]]
# New Adjacency List: {0=>[1, 2], 1=>[0, 2, 3], 2=>[1, 0], 3=>[1, 4], 4=>[3, 5], 5=>[4]}
# Connected component: [0, 1, 2, 3, 4, 5]
# Component count: 1

# ------------------
# Starting Connections: [[1, 0], [2, 0], [3, 2], [4, 2], [4, 3], [3, 0], [4, 0]]
# Starting Adjacency List: {1=>[0], 0=>[1, 2, 3, 4], 2=>[0, 3, 4], 3=>[2, 4, 0], 4=>[2, 3, 0]}
# Connected component: [1, 0, 2, 3, 4]
# Starting # of components: 1

# Delete [1, 0]
# New Connections: [[1, 1], [2, 0], [3, 2], [4, 2], [4, 3], [3, 0], [4, 0]]
# New Adjacency List: {1=>[1, 1], 2=>[0, 3, 4], 0=>[2, 3, 4], 3=>[2, 4, 0], 4=>[2, 3, 0]}
# Connected component: [1]
# Connected component: [2, 0, 3, 4]
# Component count: 2

# Delete [2, 0]
# New Connections: [[1, 0], [3, 2], [4, 2], [4, 3], [3, 0], [4, 0]]
# New Adjacency List: {1=>[0], 0=>[1, 3, 4], 3=>[2, 4, 0], 2=>[3, 4], 4=>[2, 3, 0]}
# Connected component: [1, 0, 3, 2, 4]
# Component count: 1

# Delete [3, 2]
# New Connections: [[1, 0], [2, 0], [4, 2], [4, 3], [3, 0], [4, 0]]
# New Adjacency List: {1=>[0], 0=>[1, 2, 3, 4], 2=>[0, 4], 4=>[2, 3, 0], 3=>[4, 0]}
# Connected component: [1, 0, 2, 4, 3]
# Component count: 1

# Delete [4, 2]
# New Connections: [[1, 0], [2, 0], [3, 2], [4, 3], [3, 0], [4, 0]]
# New Adjacency List: {1=>[0], 0=>[1, 2, 3, 4], 2=>[0, 3], 3=>[2, 4, 0], 4=>[3, 0]}
# Connected component: [1, 0, 2, 3, 4]
# Component count: 1

# Delete [4, 3]
# New Connections: [[1, 0], [2, 0], [3, 2], [4, 2], [3, 0], [4, 0]]
# New Adjacency List: {1=>[0], 0=>[1, 2, 3, 4], 2=>[0, 3, 4], 3=>[2, 0], 4=>[2, 0]}
# Connected component: [1, 0, 2, 3, 4]
# Component count: 1

# Delete [3, 0]
# New Connections: [[1, 0], [2, 0], [3, 2], [4, 2], [4, 3], [4, 0]]
# New Adjacency List: {1=>[0], 0=>[1, 2, 4], 2=>[0, 3, 4], 3=>[2, 4], 4=>[2, 3, 0]}
# Connected component: [1, 0, 2, 3, 4]
# Component count: 1

# Delete [4, 0]
# New Connections: [[1, 0], [2, 0], [3, 2], [4, 2], [4, 3], [3, 0]]
# New Adjacency List: {1=>[0], 0=>[1, 2, 3], 2=>[0, 3, 4], 3=>[2, 4, 0], 4=>[2, 3]}
# Connected component: [1, 0, 2, 3, 4]
# Component count: 1
