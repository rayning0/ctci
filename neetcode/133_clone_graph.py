# https://leetcode.com/problems/clone-graph/
# https://neetcode.io/solutions/clone-graph
# DFS: visited clone map

from graph_helper import Node, graphToAdjList
from collections import deque

# DFS
# Time: O(V + E), since each node is cloned once and each adjacency-list item is examined once.
# Space: O(V), for dictionary and recursion stack, excluding the cloned graph itself.
# V = # of vertices, E = # of edges
def cloneGraph(node: Optional['Node']) -> Optional['Node']:
    if not node:
        return None

    clones = {} # dictionary, old Node -> cloned Node
    # Failing to track visited nodes causes infinite recursion if graph contains cycles.
    # Always use map to store already-cloned nodes, before processing neighbors.

    # dfs(old_node) returns the one and only cloned Node of old_node.
    def dfs(old_node):
        # if old_node was already cloned, return its clone
        if old_node in clones:
            return clones[old_node]

        # otherwise, clone old_node and add its clone to dictionary
        new_node = Node(old_node.val)

        # Why must this line happen BEFORE looping through old_node's neighbors?
        # Because the graph can contain CYCLES, and DFS must know if a node's clone already
        # exists before recursively visiting its neighbors. When recursively traversing a graph
        # with cycles, mark a node as discovered BEFORE exploring its neighbors, not after.
        clones[old_node] = new_node

        for old_neighbor in old_node.neighbors:
            new_neighbor = dfs(old_neighbor)
            new_node.neighbors.append(new_neighbor)

        return new_node

    return dfs(node)

# Only dfs() should create cloned nodes.
# The caller should never independently create a clone of a neighbor. It should request the clone from DFS.
# This ensures that:
# - Every original node gets exactly one clone.
# - Every edge points to the correct clone.
# - Cycles don't cause infinite recursion.
# - Multiple nodes sharing a neighbor reference the same cloned object.

if __name__ == "__main__":
    # 1 ----- 2
    # |       |
    # |       |
    # 4 ----- 3
    # adjList = [[2,4],[1,3],[2,4],[1,3]]

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]

    clone = cloneGraph(n1)

    assert graphToAdjList(clone) == [[2,4],[1,3],[2,4],[1,3]]
    # Verify deep copy
    assert clone is not n1
    assert clone.neighbors[0] is not n2
    assert clone.neighbors[1] is not n4

    # Graph has only 1 node with val = 1 and no neighbors. Empty list.
    # adjList = [[]]

    n1 = Node(1)
    clone = cloneGraph(n1)

    assert graphToAdjList(clone) == [[]]
    # Verify deep copy
    assert clone is not n1

    # Empty graph with no nodes.
    # adjList = []

    assert cloneGraph(None) is None
    assert graphToAdjList(cloneGraph(None)) == []

    # 1 ----- 2 ----- 3
    # adjList = [[2],[1,3],[2]]

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    n1.neighbors = [n2]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2]

    clone = cloneGraph(n1)

    assert graphToAdjList(clone) == [[2],[1,3],[2]]
    # Verify deep copy
    assert clone is not n1
    assert clone.neighbors[0] is not n2
    print("All tests passed!")
