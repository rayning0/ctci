# https://leetcode.com/problems/set-matrix-zeroes/description/
# https://neetcode.io/problems/set-zeroes-in-matrix/solution

# To create empty 2D matrix, use list comprehension:
# m = arr = [[0] * cols for _ in range(rows)]

# 1. Iteration. (EASY TO REMEMBER!) Solve in 2 phases:

# Pass 1: Loop through all cells to find all 0's. Use 2 helper arrays: rows[], cols[].
# Set rows[r] = True if row r should be zeroed.
# Set cols[c] = True if col c should be zeroed.

# Pass 2: Loop through all cells again. If rows[r] or rows[c] == True, matrix[r][c] = 0.
#
# Time: O(m * n), Space: O(m + n)
def setZeroes(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    # print("Before:")
    # pp(matrix)

    ROWS, COLS = len(matrix), len(matrix[0])
    rows, cols = [False] * ROWS, [False] * COLS

    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                rows[r] = True
                cols[c] = True

    for r in range(ROWS):
        for c in range(COLS):
            if rows[r] or cols[c]:
                matrix[r][c] = 0

    # print("After:")
    # pp(matrix)
    # print()

# 2. Iteration (HARD TO REMEMBER, but only O(1) space). Use input matrix ITSELF to store location of original 0s.

# Pass 1: Loop through all cells to find all 0's.
# Use matrix row 0 to mark which columns should be 0
# If r > 0, use matrix col 0 to mark which rows should be 0
# If r == 0, separately use row_zero boolean var to track if row 0 should be 0.
# Since matrix[0][0] is intersection of row 0 and col 0, it can't independently represent both.

# Pass 2: Based on markers, apply 0s to right row/cols in matrix.
# Time: O(m * n), Space: O(1)
def setZeroes(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    print("Before:")
    pp(matrix)

    row_zero = False
    ROWS, COLS = len(matrix), len(matrix[0])
    rows, cols = [False] * ROWS, [False] * COLS

    # Pass 1:
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                matrix[0][c] = 0        # mark col that should be 0

                if r > 0:
                    matrix[r][0] = 0    # mark row that should be 0
                else:
                    row_zero = True     # row 0 should be 0.
    # Since we using matrix[0] to track which cols should be 0, we must use
    # separate boolean var "row_zero" to track if row 0 should be 0.

    # matrix = [
    #     [1,2,3],
    #     [4,0,5],
    #     [6,7,8]
    # ]

    # matrix = [
    #     [1,0,3],
    #     [0,0,5], <-- r = 1
    #     [6,7,8]
    # ]      c = 1

    # Pass 2:
    for r in range(1, ROWS):
        for c in range(1, COLS):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    if matrix[0][0] == 0:
        for r in range(ROWS):
            matrix[r][0] = 0

    if row_zero:
        for c in range(COLS):
            matrix[0][c] = 0  # set all row 0 to 0

    print("After:")
    pp(matrix)
    print()

# pretty print 2D matrix
def pp(matrix: list[list[int]]) -> None:
    for row in matrix:
        print(*row) # * unpacks elements from an iterable

if __name__ == "__main__":
    matrix = [[0,1],[1,0]]
    setZeroes(matrix)
    assert matrix == [[0,0],[0,0]]

    matrix = [
        [1,2,3],
        [4,0,5],
        [6,7,8]
    ]
    setZeroes(matrix)
    assert matrix == [
                [1,0,3],
                [0,0,0],
                [6,0,8]
           ]

    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    setZeroes(matrix)
    assert matrix == [[1,0,1],[0,0,0],[1,0,1]]

    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    setZeroes(matrix)
    assert matrix == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    print("All tests passed!")
