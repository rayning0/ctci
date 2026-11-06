# https://leetcode.com/problems/rotting-oranges/description/
# https://neetcode.io/solutions/rotting-oranges
# BFS with levels

# 0 = empty cell, 1 = fresh orange, 2 = rotten orange
# Each minute, any fresh orange adjacent (in 4 directions) to rotten orange becomes rotten
# Return min of minutes till NO cell has a fresh orange. If it's impossible, return -1.

from collections import deque
# Time: O(m * n), Space: O(m * n)
def orangesRotting(grid: list[list[int]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque()
    time = 0
    fresh = 0

    # Push coordinates of all rotten oranges into queue.
    # Count fresh oranges to know when all have rotted or when some unreachable.
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 2:
                q.append((r, c))
            if grid[r][c] == 1:
                fresh += 1

    # "while q" alone is not enough here, since loop only ends when queue is empty.
    # But when all oranges turn rotten, we still add last rotten orange to queue.
    # Thus while loop would run 1 more time (1 more min), which is wrong!
    # So use "while q and fresh > 0" to stop loop when no more fresh oranges.
    while q and fresh > 0:
        size = len(q)
        # Since we care which BFS level a node is on, must use for-loop!
        for _ in range(size):
            r, c = q.popleft()
            for dr, dc in moves:
                nr, nc = r + dr, c + dc

                #     if new cell is on grid         and   fresh orange
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                    grid[nr][nc] = 2    # make it rotten
                    fresh -= 1
                    q.append((nr, nc))
        time += 1
        # print(f"Time: {time}")
        # pp(grid)

    # Edge case: If fresh oranges remain after BFS, no reachable rotten orange can infect them
    if fresh > 0:
        return -1

    return time

# pretty print grid
def pp(grid):
    for row in grid:
        print(*row)

if __name__ == "__main__":
    assert orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4
    assert orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1
    assert orangesRotting([[0,2]]) == 0
    assert orangesRotting([[1,1,0],[0,1,1],[0,1,2]]) == 4
    assert orangesRotting([[1,0,1],[0,2,0],[1,0,1]]) == -1
    print("All tests passed!")

# Output of each test

# Time: 0
# 2 1 1
# 1 1 0
# 0 1 1
# Time: 1
# 2 2 1
# 2 1 0
# 0 1 1
# Time: 2
# 2 2 2
# 2 2 0
# 0 1 1
# Time: 3
# 2 2 2
# 2 2 0
# 0 2 1
# Time: 4
# 2 2 2
# 2 2 0
# 0 2 2
#--------
# Time: 0
# 2 1 1
# 0 1 1
# 1 0 1
# Time: 1
# 2 2 1
# 0 1 1
# 1 0 1
# Time: 2
# 2 2 2
# 0 2 1
# 1 0 1
# Time: 3
# 2 2 2
# 0 2 2
# 1 0 1
# Time: 4
# 2 2 2
# 0 2 2
# 1 0 2
# Time: 5
# 2 2 2
# 0 2 2
# 1 0 2
#--------
# Time: 0
# 0 2
#--------
# Time: 0
# 1 1 0
# 0 1 1
# 0 1 2
# Time: 1
# 1 1 0
# 0 1 2
# 0 2 2
# Time: 2
# 1 1 0
# 0 2 2
# 0 2 2
# Time: 3
# 1 2 0
# 0 2 2
# 0 2 2
# Time: 4
# 2 2 0
# 0 2 2
# 0 2 2
#--------
# Time: 0
# 1 0 1
# 0 2 0
# 1 0 1
# Time: 1
# 1 0 1
# 0 2 0
# 1 0 1

Does a problem care which BFS level a node belongs to?

No: Use ordinary BFS with "while q".
Yes: Use "size = len(q)" and a for loop, unless you're tracking distance separately.
All currently rotten oranges spread infection simultaneously each minute. That's why level-by-level BFS is the natural solution.

<2 types of BFS problems>

1. BFS without levels: Use when you only must visit/process each node and don't care about levels.

while q:
    node = q.popleft()

    for neighbor in neighbors(node):
        if neighbor not in visited:
            visited.add(neighbor)
            q.append(neighbor)

2. BFS with levels: Use when you must know where each distance layer ends and the next begins.

while q:
    size = len(q)

    for _ in range(size):
        node = q.popleft()

        for neighbor in neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)

    # One entire BFS level completed


Problem	                                    Level loop?	  Reason
LC 102 — Binary Tree Level Order Traversal	Yes	          Group nodes by tree depth
LC 200 — Number of Islands	                No	          Just explore each island
LC 133 — Clone Graph (BFS)	                No	          Just clone reachable nodes
LC 994 — Rotting Oranges	                Yes	          Each level represents 1 minute
LC 797 — All Paths (BFS alternative)	    No	          Track complete paths, not levels
