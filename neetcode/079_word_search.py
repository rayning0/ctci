# https://leetcode.com/problems/word-search/description/
# https://neetcode.io/solutions/word-search
# Backtracking: Grid DFS

# m = rows, n = columns, L = len(word)
# Time: O(m * n * 3^L)
# Space: O( min(L, m * n) )
def exist(board: list[list[str]], word: str) -> bool:
    ROWS, COLS = len(board), len(board[0])
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = set()

    def dfs(r, c, i):               # i = current index for character we seek in "word"
        if (r, c) in visited or board[r][c] != word[i]:
            return False

        visited.add((r, c))

        if i == len(word) - 1:          # successfully found end of word!
            return True

        for dr, dc in moves:            # Explore all adjacent cells
            nr, nc = r + dr, c + dc

            if 0 <= nr < ROWS and 0 <= nc < COLS:
                if dfs(nr, nc, i + 1):  # seek next character (i + 1) in word
                    return True

        visited.remove((r, c))          # Backtrack after explore all neighbors
        return False

    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0):
                return True

    return False

# Why is Time: O(m * n * 3^L)?
# Nested for loop (ROWS, COLS) is O(m * n).
# Each dfs() explores 4 directions, but due to visited{},
# we explore only 3 directions for each cell. So O(3^L).

# Why is Space: O(min(L, m*n))? It depends on max length of 1 DFS path.
# Due to backtracking, visited{} only keeps cells on current DFS path. Can't exceed L or m*n.
# Each DFS recursive call adds 1 to word index. Max recursion depth = min(L, m*n).

# pretty print grid
def pp(grid):
    for row in grid:
        print(*row)

if __name__ == '__main__':
    assert exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED") is True
    assert exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE") is True
    assert exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB") is False
    assert exist([
        ["A","B","C","D"],
        ["S","A","A","T"],
        ["A","C","A","E"]
    ], "CAT") is True
    assert exist([
        ["A","B","C","D"],
        ["S","A","A","T"],
        ["A","C","A","E"]
    ], "BAT") is False
    print('All tests passed!')

# Output for each test:

# (r, c, i) = (0, 0, 0)
# Found word[0] = A. visited: {(0, 0)}
# (r, c, i) = (1, 0, 1)
# (r, c, i) = (0, 1, 1)
# Found word[1] = B. visited: {(0, 1), (0, 0)}
# (r, c, i) = (1, 1, 2)
# (r, c, i) = (0, 2, 2)
# Found word[2] = C. visited: {(0, 1), (0, 2), (0, 0)}
# (r, c, i) = (1, 2, 3)
# Found word[3] = C. visited: {(0, 1), (0, 2), (1, 2), (0, 0)}
# (r, c, i) = (2, 2, 4)
# Found word[4] = E. visited: {(0, 1), (1, 2), (0, 0), (0, 2), (2, 2)}
# (r, c, i) = (2, 3, 5)
# (r, c, i) = (2, 1, 5)
# Found word[5] = D. visited: {(0, 1), (1, 2), (2, 1), (0, 0), (0, 2), (2, 2)}
# a b c E
# S F c S
# A d e E
# --------------------------
# (r, c, i) = (0, 0, 0)
# (r, c, i) = (0, 1, 0)
# (r, c, i) = (0, 2, 0)
# (r, c, i) = (0, 3, 0)
# (r, c, i) = (1, 0, 0)
# Found word[0] = S. visited: {(1, 0)}
# (r, c, i) = (2, 0, 1)
# (r, c, i) = (0, 0, 1)
# (r, c, i) = (1, 1, 1)
# Didn't find word. Backtrack: Remove (1, 0)
# (r, c, i) = (1, 1, 0)
# (r, c, i) = (1, 2, 0)
# (r, c, i) = (1, 3, 0)
# Found word[0] = S. visited: {(1, 3)}
# (r, c, i) = (2, 3, 1)
# Found word[1] = E. visited: {(2, 3), (1, 3)}
# (r, c, i) = (2, 2, 2)
# Found word[2] = E. visited: {(2, 3), (1, 3), (2, 2)}
# A B C E
# s F C s
# A D e e
# --------------------------
# (r, c, i) = (0, 0, 0)
# Found word[0] = A. visited: {(0, 0)}
# (r, c, i) = (1, 0, 1)
# (r, c, i) = (0, 1, 1)
# Found word[1] = B. visited: {(0, 1), (0, 0)}
# (r, c, i) = (1, 1, 2)
# (r, c, i) = (0, 2, 2)
# Found word[2] = C. visited: {(0, 1), (0, 2), (0, 0)}
# (r, c, i) = (1, 2, 3)
# (r, c, i) = (0, 3, 3)
# Didn't find word. Backtrack: Remove (0, 2)
# Didn't find word. Backtrack: Remove (0, 1)
# Didn't find word. Backtrack: Remove (0, 0)
# (r, c, i) = (0, 1, 0)
# (r, c, i) = (0, 2, 0)
# (r, c, i) = (0, 3, 0)
# (r, c, i) = (1, 0, 0)
# (r, c, i) = (1, 1, 0)
# (r, c, i) = (1, 2, 0)
# (r, c, i) = (1, 3, 0)
# (r, c, i) = (2, 0, 0)
# Found word[0] = A. visited: {(2, 0)}
# (r, c, i) = (1, 0, 1)
# (r, c, i) = (2, 1, 1)
# Didn't find word. Backtrack: Remove (2, 0)
# (r, c, i) = (2, 1, 0)
# (r, c, i) = (2, 2, 0)
# (r, c, i) = (2, 3, 0)
# --------------------------
# (r, c, i) = (0, 0, 0)
# (r, c, i) = (0, 1, 0)
# (r, c, i) = (0, 2, 0)
# Found word[0] = C. visited: {(0, 2)}
# (r, c, i) = (1, 2, 1)
# Found word[1] = A. visited: {(0, 2), (1, 2)}
# (r, c, i) = (2, 2, 2)
# (r, c, i) = (1, 3, 2)
# Found word[2] = T. visited: {(0, 2), (1, 2), (1, 3)}
# A B c D
# S A a t
# A C A E
# --------------------------
# (r, c, i) = (0, 0, 0)
# (r, c, i) = (0, 1, 0)
# Found word[0] = B. visited: {(0, 1)}
# (r, c, i) = (1, 1, 1)
# Found word[1] = A. visited: {(0, 1), (1, 1)}
# (r, c, i) = (2, 1, 2)
# (r, c, i) = (1, 2, 2)
# (r, c, i) = (1, 0, 2)
# Didn't find word. Backtrack: Remove (1, 1)
# (r, c, i) = (0, 2, 1)
# (r, c, i) = (0, 0, 1)
# Found word[1] = A. visited: {(0, 1), (0, 0)}
# (r, c, i) = (1, 0, 2)
# Didn't find word. Backtrack: Remove (0, 0)
# Didn't find word. Backtrack: Remove (0, 1)
# (r, c, i) = (0, 2, 0)
# (r, c, i) = (0, 3, 0)
# (r, c, i) = (1, 0, 0)
# (r, c, i) = (1, 1, 0)
# (r, c, i) = (1, 2, 0)
# (r, c, i) = (1, 3, 0)
# (r, c, i) = (2, 0, 0)
# (r, c, i) = (2, 1, 0)
# (r, c, i) = (2, 2, 0)
# (r, c, i) = (2, 3, 0)

<General Backtracking Algorithm>

def dfs(state):
    if is_solution(state):
        record_solution(state)
        return

    for choice in get_choices(state):
        if not is_valid(choice, state):
            continue

        make_choice(choice, state)    # CHOOSE
        dfs(state)                    # EXPLORE
        undo_choice(choice, state)    # BACKTRACK

For problems returning True/False early, like this one:

def dfs(state):
    if is_invalid(state):
        return False

    if is_solution(state):
        return True

    mark_choice(state)

    for next_state in get_choices(state):
        if dfs(next_state):
            return True

    undo_choice(state)  # Backtrack on failure
    return False

How to recognize backtracking problems:

Backtracking is especially useful to explore multiple possible choices,
where an unsuccessful choice must be undone so another can be tried.

Examples:
- LC 79 Word Search: Try neighboring cells; undo visited marks on failure.
- LC 46 Permutations: Choose an unused number; remove it from the current permutation afterward.
- LC 78 Subsets: Include or exclude an element; undo selections as needed.
- LC 39 Combination Sum: Choose a candidate; undo it before trying another combination.
- LC 51 N-Queens: Place a queen; remove it when exploring another placement.

An important difference from ordinary DFS: backtracking explores a search tree of possible decisions. The same graph cell/candidate can participate in different branches, even though it cannot be reused in 1 invalid path.
