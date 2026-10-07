# https://leetcode.com/problems/number-of-islands/description/
# https://neetcode.io/solutions/number-of-islands
# Graph DFS / BFS: Flood Fill

# Either solution works! Both have same Big O.

# | DFS               | BFS                 |
# |-------------------|---------------------|
# | dfs(r, c)         | q = deque([(r, c)]) |
# | mark visited      | mark visited        |
# | recurse neighbors | enqueue neighbors   |

# DFS
# 1. Scan through row + cols of grid.
# 2. Found land? ('1')
# 3. If yes, we found new island! count += 1
# 4. Use DFS to ERASE entire island: Set all its adjacent land cells to '0'.
# 5. Keep scanning rest of grid for new land.

# Separation of responsibilities:
# - Outer loops count islands.
# - DFS destroys an island.
# - Neither does the other's job.

# 1. DFS
# Time: O(m * n)
# Space: O(m * n) worst case, since recursion for DFS keeps big # of calls on a stack before unwinding.
# m, n = # of rows, # of cols
def numIslands(grid: list[list[str]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    count = 0
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Flood-fill island by erasing every connected land cell.
    def dfs(r, c):
        #       if cell is on grid         and   unvisited land
        if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == '1':
            grid[r][c] = '0'               # mark it as visited

            # Flood-fill its 4 neighbor cells
            for dr, dc in moves:
                dfs(r + dr, c + dc)

    # Outer loops find FIRST CELL of each island
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == '1':   # found new island!
                count += 1
                dfs(r, c)           # erase all land cells for that island

    return count

#------------------------------------------------------
from collections import deque

# 2. BFS
# Time: O(m * n)
# Space: O(m * n) worst case
# m, n = # of rows, # of cols
def numIslands(grid: list[list[str]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    count = 0
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == '1':   # found new island!
                count += 1

                q = deque([(r, c)])
                grid[r][c] = '0'    # mark cell as visited
                while q:
                    r, c = q.popleft()

                    for dr, dc in moves:        # for each neighbor
                        nr, nc = r + dr, c + dc

                        #       if neighbor is on grid       and    unvisited
                        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == '1':
                            grid[nr][nc] = '0'  # mark it as visited
                            q.append((nr, nc))  # add it to queue

    return count

# pretty print grid
def pp(grid):
    for row in grid:
        print(*row)

if __name__ == "__main__":
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    assert numIslands(grid) == 1

    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    assert numIslands(grid) == 3

    grid = [
        ["0","1","1","1","0"],
        ["0","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    assert numIslands(grid) == 1

    grid = [
        ["1","1","0","0","1"],
        ["1","1","0","0","1"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    assert numIslands(grid) == 4
    print("All tests passed!")

# BFS Pattern:

# q = deque([(start)])

# mark start visited

# while q:
#     pop

#     for each neighbor:
#         if neighbor is valid and unvisited:
#             mark visited
#             enqueue

# This BFS template works for huge number of graph problems:
# - LC 200 Number of Islands
# - LC 695 Max Area of Island
# - LC 994 Rotting Oranges
# - LC 286 Walls and Gates
# - Shortest-path grid problems (with minor changes)
