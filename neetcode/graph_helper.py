class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque

# Convert graph to LeetCode adjacency list format. Uses BFS.
# Time: O(V + E)
# Space: O(V)
def graphToAdjList(node: Node | None) -> list[list[int]]:
    if not node:
        return []

    adj = {}
    visited = set()
    visited.add(node)
    q = deque([node])

    while q:
        curr = q.popleft()

        # LeetCode adjacency list stores only neighbor values.
        adj[curr.val] = [neighbor.val for neighbor in curr.neighbors]

        for neighbor in curr.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)

    # LeetCode assumes node values are 1..N.
    return [adj[i] for i in range(1, len(adj) + 1)]
