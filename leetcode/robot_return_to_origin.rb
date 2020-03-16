# https://leetcode.com/problems/robot-return-to-origin/
def judge_circle(moves)
    dir = {'R' => [0, 1], 'L' => [0, -1], 'D' => [1, 0], 'U' => [-1, 0]}
    row, col = 0, 0
    moves.each_char do |move|
        drow, dcol = dir[move]
        row += drow
        col += dcol
    end

    return true if row == 0 && col == 0
    false
end
