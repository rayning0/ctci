# https://leetcode.com/problems/all-paths-from-source-to-target/description/?envType=company&envId=netflix&favoriteSlug=netflix-all
# https://algo.monster/liteproblems/797
# DFS with backtracking: Path Enumeration

# Given directed acyclic graph (DAG) of n nodes labeled 0 to n - 1,
# find all possible paths from node 0 to node n - 1 and return them in any order.
# graph[i] is list of all nodes you can visit from node i (i.e., node i -> node graph[i][j]).

# Backtracking is DFS through a decision tree, undoing changes when returning from each branch:
# def dfs(...):
#     if base_case:
#         record_solution()
#         return

#     for choice in choices:
#         choose(choice)
#         dfs(...)
#         undo(choice)

# Time:  O(2^n * n) in worst case. Every time we add new node to the graph, the number of paths doubles: 1 with new node, 1 without it.
# Space: O(n) auxiliary. Total space: O(2^n * n)
# Time is O(2^n * n) since a DAG can have exponentially many paths from source to target, and copying each path takes up to O(n) time.
# Auxiliary space is O(n) for current path + recursion stack. Including the stored results, total space = O(2^n * n)
def allPathsSourceTarget(graph: list[list[int]]) -> list[list[int]]:
    target = len(graph) - 1
    paths = []
    path = [0]

    def dfs(node):
        # Base case
        if node == target:
            paths.append(path.copy())
            # Use path.copy(), not path, since when we change path later (path.pop()), it also changes path in paths!
            # path.copy(), path[:], or list(path) are all OK. All make shallow copies of path.
            return

        # Backtracking
        for n in graph[node]:
            path.append(n)  # Choose
            dfs(n)          # Explore
            path.pop()      # Undo

    dfs(0)
    return paths

# Example:  graph = [[1, 2], [3], [3], []]
# start dfs(0). path: [0]
# Using 1 in for loop.
# start dfs(1). path: [0, 1]
# Using 3 in for loop.
# start dfs(3). path: [0, 1, 3]
# found path: [0, 1, 3]. paths: [[0, 1, 3]]
# left dfs. path: [0, 1, 3]. paths: [[0, 1, 3]]
# pop 3. path: [0, 1]
# left dfs. path: [0, 1]. paths: [[0, 1, 3]]
# pop 1. path: [0]
# Using 2 in for loop.
# start dfs(2). path: [0, 2]
# Using 3 in for loop.
# start dfs(3). path: [0, 2, 3]
# found path: [0, 2, 3]. paths: [[0, 1, 3], [0, 2, 3]]
# left dfs. path: [0, 2, 3]. paths: [[0, 1, 3], [0, 2, 3]]
# pop 3. path: [0, 2]
# left dfs. path: [0, 2]. paths: [[0, 1, 3], [0, 2, 3]]
# pop 2. path: [0]
# final paths: [[0, 1, 3], [0, 2, 3]]

if __name__ == "__main__":
    # use sorted() since paths may be returned in any order
    assert allPathsSourceTarget([[1,2],[3],[3],[]]) == [[0,1,3],[0,2,3]]
    assert allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]) == [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
    print("All tests passed!")

# Example:  graph = [[4,3,1],[3,2,4],[3],[4],[]]
# start dfs(0). path: [0]
# Using 4 in for loop.
# start dfs(4). path: [0, 4]
# found path: [0, 4]. paths: [[0, 4]]
# left dfs. path: [0, 4]. paths: [[0, 4]]
# pop 4. path: [0]
# Using 3 in for loop.
# start dfs(3). path: [0, 3]
# Using 4 in for loop.
# start dfs(4). path: [0, 3, 4]
# found path: [0, 3, 4]. paths: [[0, 4], [0, 3, 4]]
# left dfs. path: [0, 3, 4]. paths: [[0, 4], [0, 3, 4]]
# pop 4. path: [0, 3]
# left dfs. path: [0, 3]. paths: [[0, 4], [0, 3, 4]]
# pop 3. path: [0]
# Using 1 in for loop.
# start dfs(1). path: [0, 1]
# Using 3 in for loop.
# start dfs(3). path: [0, 1, 3]
# Using 4 in for loop.
# start dfs(4). path: [0, 1, 3, 4]
# found path: [0, 1, 3, 4]. paths: [[0, 4], [0, 3, 4], [0, 1, 3, 4]]
# left dfs. path: [0, 1, 3, 4]. paths: [[0, 4], [0, 3, 4], [0, 1, 3, 4]]
# pop 4. path: [0, 1, 3]
# left dfs. path: [0, 1, 3]. paths: [[0, 4], [0, 3, 4], [0, 1, 3, 4]]
# pop 3. path: [0, 1]
# Using 2 in for loop.
# start dfs(2). path: [0, 1, 2]
# Using 3 in for loop.
# start dfs(3). path: [0, 1, 2, 3]
# Using 4 in for loop.
# start dfs(4). path: [0, 1, 2, 3, 4]
# found path: [0, 1, 2, 3, 4]. paths: [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4]]
# left dfs. path: [0, 1, 2, 3, 4]. paths: [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4]]
# pop 4. path: [0, 1, 2, 3]
# left dfs. path: [0, 1, 2, 3]. paths: [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4]]
# pop 3. path: [0, 1, 2]
# left dfs. path: [0, 1, 2]. paths: [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4]]
# pop 2. path: [0, 1]
# Using 4 in for loop.
# start dfs(4). path: [0, 1, 4]
# found path: [0, 1, 4]. paths: [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
# left dfs. path: [0, 1, 4]. paths: [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
# pop 4. path: [0, 1]
# left dfs. path: [0, 1]. paths: [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
# pop 1. path: [0]
# final paths: [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]

# 1. Could we use BFS to solve this?

# Yes, but BFS must keep multiple partial paths in memory simultaneously.
# Use DFS instead.

# DFS only must maintain the CURRENT path along its recursion stack, plus the completed paths you've collected.
# Both algorithms must enumerate every valid path, so neither avoids the potentially exponential output size.

# 	                    BFS	                    DFS with backtracking
# Finds all paths	        Yes	                    Yes
# Stores partial paths	Many in queue	        1 current path
# Traversal order	        Shorter paths first	    Depth-first
# Memory efficiency	    Often worse	            Usually better
# Natural fit	            Shortest-path problems	All-path enumeration

# BFS isn't incorrect or asymptotically worse in every case.
# We prefer DFS here because it can reuse 1 mutable path rather than storing many path copies.

# BFS example: Arrows point left to right: 0 -> 1 -> 3 and 0 -> 2 -> 3
#     1
#   /   \
# 0       3
#   \   /
#     2

# graph = [[1, 2], [3], [3], []]
# answer = [[0, 1, 3], [0, 2, 3]]

# With BFS, instead of putting individual nodes in your queue, you could put entire paths:
# q = deque([[0]])
# Queue:
# [[0]]

# Expand 0:
# [[0,1], [0,2]]

# Expand 1:
# [[0,2], [0,1,3]]

# Expand 2:
# [[0,1,3], [0,2,3]]
# Whenever a path reaches the target, add it to your results.

# 2. What's difference between DFS vs. DFS with backtracking?

# In DFS, our goal is to explore reachable nodes.
# Once we visit a node, we usually don't need to visit it again.

# In DFS with backtracking, we're exploring possible paths

# We don't ask: Which nodes can I reach?
# We ask: What are all different paths I can take to reach target?

# So a node may need to appear in MULTIPLE different paths.

# If we used a global visited set and skip previously visited nodes, we could eliminate valid paths.
# Instead, we must keep a path list representing your current route.

# 3. What does "backtracking" mean?

# Make a choice, explore it, undo that choice, then try another choice.

# path.append(next_node)  # Make a choice
# dfs(next_node)          # Explore
# path.pop()              # Undo the choice

# How current path changes:
# 0
# 0 -> 1
# 0 -> 1 -> 3. Found target, Path 1.
# 0 -> 1. Backtrack.
# 0. Backtrack.
# 0 -> 2
# 0 -> 2 -> 3. Found target, Path 2.

# ----------------------------------------------------
# What's difference between path.copy(), path[:], and list(path)?

# For your case — a list of ints — **all 3 do exactly the same thing**: return a new, independent list with the same elements,
# in O(n). The differences show up in what they *accept* and what they *return*.

#               | Accepts          | Returns    | Notes
# `path.copy()` | list only        | `list`     | Most explicit about intent. Added in Python 3.3.
# `path[:]`     | any **sequence** | same type  | Slicing. `tup[:]` → tuple, `s[:]` → str.
# `list(path)`  | any **iterable** | `list`     | Also converts: `list({1,2})`, `list(gen())`.

# So `list(x)` is most general — it will happily consume a generator, set, or dict-keys view, where `.copy()` and `[:]` would raise. And `[:]` is the only one that preserves the original type.

# ```python
# list((1,2,3))     # [1,2,3]   tuple → list
# (1,2,3)[:]        # (1,2,3)   stays a tuple
# (1,2,3).copy()    # AttributeError
# ```

# However, all 3 make SHALLOW copies of path.

# ```python
# a = [[1,2], [3]]
# b = a.copy()          # same for b = a[:], b = list(a)
# b[0].append(99)
# print(a)              # [[1,2,99], [3]]  ← inner list is shared
# ```

# The outer list is new, but nested mutable objects are still aliased. That's why it's safe in your solution — `path` holds `int`s, which are immutable — and why you'd reach for `copy.deepcopy` if it held lists.
