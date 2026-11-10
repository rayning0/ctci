# https://leetcode.com/problems/redundant-connection/
# https://neetcode.io/solutions/redundant-connection
# Union-Find

# We start with an undirected graph with:
# 1. n nodes
# 2. n edges (a tree plus 1 extra edge)
# 3. All nodes connected

# Find the 1 edge to remove to restore a tree.
# If multiple edges are possible, return the edge appearing last in the input edges.

# Final graph must be:
# 1. Connected
# 2. Acyclic (no cycles)

# A tree has minimum number of edges (n-1) needed to connect all n nodes.
# With n-1 edges, a connected graph can't afford to waste any edge creating a cycle.
# Every edge must help connect previously disconnected components.

# Ex: 4 nodes, 3 edges. The best way to use edge 3 is 2 -- 4, not 2 -- 3.
# A connected graph with exactly n-1 edges cannot have a cycle!
# 1 --- 2
#  \   /
#    3    4

# Thus after removing 1 edge (leaving n-1 edges), if graph is still connected,
# graph must be acyclic! We have our answer!

# With n-1 edges, we only have 2 possibilities:
# Still connected	    All n-1 edges needed for connectivity, so no cycle exists. We're done.
# Disconnected	    We removed an essential connection and left original cycle intact

# For undirected graph with n nodes, any 2 of 3 conditions imply the third must be true:
# 1. Graph is connected.
# 2. Graph has n-1 edges.
# 3. Graph is acyclic.

# How to check if graph is connected? Use UNION-FIND algorithm:
# Create graph 1 edge at a time. "If I add this edge, were its 2 endpoints already connected?"
# If yes, we just made a cycle.

# Union-Find tracks groups of connected nodes and supports 2 operations:
# 1. Find: Follow parent pointers to find a node's component root.
# 2. Union: Connect 2 components by making 1 root point to the other.

# Central idea of Union-Find: merge entire components by changing 1 parent pointer, not relabeling every node!

# 1. Union-Find (Optimal)
# Time: O(V + E α(V)) = O(V + V α(V)), E = V. Since α(V) nearly constant, effectively O(V).
# Space: O(V)
# V = vertices, E = edges, α = inverse Ackermann function
def findRedundantConnection(edges: list[list[int]]) -> list[int]:
    n = len(edges)
    # Initialize each node as its own separate component
    parent = {i: i for i in range(1, n + 1)}
    size = {i: 1 for i in range(1, n + 1)} # Track component sizes by roots

    # Follow parent pointers to find a node's component root.
    # Time: O(h), Space: O(1). h = max height of parent pointer tree
    def find(node):
        curr = node
        while node != parent[node]:
            node = parent[node]

        # Optimization 1. Path Compression:
        # Make all nodes on path (from curr to root) point directly to root.
        while curr != parent[curr]:
            next_node = parent[curr]
            parent[curr] = node
            curr = next_node
        return node

    # Merge 2 components by making 1 root point to the other.
    # Time: O(h), Space: O(1). h = max height of parent pointer tree
    def union(start, end):
        start_root = find(start)
        end_root = find(end)

        # New edge is redundant and would form a cycle. Done!
        if start_root == end_root:
            return False

        # Optimization 2. Union by Size: Ensure start_root is larger component
        # Attach smaller component's root to larger component's root.
        if size[start_root] < size[end_root]:
            start_root, end_root = end_root, start_root

        parent[end_root] = start_root
        size[start_root] += size[end_root]
        return True

    # Process edges in input order, merging components when you can.
    # If both nodes have same root, that edge is redundant and creates a cycle! Return it.
    for start, end in edges:
        if not union(start, end):
            return [start, end]

# 2. Union-Find (less optimal). Easier to remember!
# Time: O(V + EV) = O(V*V), since E = V
# Space: O(V)
def findRedundantConnection(edges: list[list[int]]) -> list[int]:
    n = len(edges)
    # Initialize each node as its own separate component
    parent = {i: i for i in range(1, n + 1)}

    # Follow parent pointers to find a node's component root.
    # Time: O(h), Space: O(1). h = max height of parent pointer tree, up to O(V)
    def find(node):
        while node != parent[node]:
            node = parent[node]

        return node

    # Merge 2 components by making 1 root point to the other.
    # Time: O(h), Space: O(1). h = max height of parent pointer tree, up to O(V)
    def union(start, end):
        start_root = find(start)
        end_root = find(end)

        # New edge is redundant and would form a cycle. Done!
        if start_root == end_root:
            return False

        parent[end_root] = start_root
        return True

    # Process edges in input order, merging components when you can.
    # If both nodes have same root, that edge is redundant and creates a cycle! Return it.
    for start, end in edges:
        if not union(start, end):
            return [start, end]

# 3. Connected-component labeling. Not optimal.
# Time: O(N*N), Space: O(N). N = # of nodes
# def findRedundantConnection(edges: list[list[int]]) -> list[int]:
#     group = {}
#     for start, end in edges:
#         if start not in group and end not in group:
#             group[start] = start
#             group[end] = start
#         elif start in group and end not in group:
#             group[end] = group[start]
#         elif start not in group and end in group:
#             group[start] = group[end]

#         else:  # both start and end in group
#             start_group, end_group = group[start], group[end]

#             # we just made a cycle. this new edge is redundant. return it!
#             if start_group == end_group:
#                 return [start, end]
#             else:
#                 # merge both groups
#                 for k, v in group.items():
#                     if v == end_group:
#                         group[k] = start_group

# 4. BFS solution. Not optimal. "If I remove this edge, can I still reach every node?"

# 1. Starting graph is connected and cyclic: n nodes, n edges.
# 2. Loop backwards in edges, from last to first added. Remove 1 edge at a time.
# 3. After each edge removed (i.e. n-1 edges), if graph is still connected (BFS), we're done! Return that edge.
# 3. If resulting graph not connected, move to new graph without the next edge.
# from collections import deque
# Time: O(N*N)
# Space: O(N), N = # of nodes
# def findRedundantConnection(edges: list[list[int]]) -> list[int]:
#     for i in range(len(edges) - 1, -1, -1):
#         remaining = edges[:i] + edges[i+1:] # use slice to leave out edges[i]

#         if is_connected(remaining):
#             return edges[i]

# def is_connected(remaining):
#     # map each edge in both directions, start -> end, end -> start
#     emap = {}
#     for start, end in remaining:
#         emap.setdefault(start, set()).add(end)
#         emap.setdefault(end, set()).add(start)

#     # BFS
#     visited = {remaining[0][0]}
#     q = deque([remaining[0][0]])
#     while q:
#         node = q.popleft()
#         for neighbor in emap[node]:
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 q.append(neighbor)

#     return len(visited) == len(remaining) + 1

# remaining: [[1, 2], [2, 3], [3, 4], [1, 5]]
# emap: {1: {2, 5}, 2: {1, 3}, 3: {2, 4}, 4: {3}, 5: {1}}

if __name__ == '__main__':
    assert findRedundantConnection([[1,2],[1,3],[2,3]]) == [2,3]
    assert findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]) == [1,4]
    assert findRedundantConnection([[1,2],[1,3],[3,4],[2,4]]) == [2,4]
    assert findRedundantConnection([[1,2],[1,3],[1,4],[3,4],[4,5]]) == [3,4]
    print('All tests passed!')
