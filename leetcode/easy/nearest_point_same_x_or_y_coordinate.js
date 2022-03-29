// https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/
// https://leetcode.com/submissions/detail/669787506/
// Runtime: 142 ms, faster than 40.59 % of JavaScript online submissions for Find Nearest Point That Has the Same X or Y Coordinate.
// Memory Usage: 51.3 MB, less than 10.89 % of JavaScript online submissions for Find Nearest Point That Has the Same X or Y Coordinate.
// O(n) time, O(1) space
// Time to write code: 3:49 min. (Original time to code: 22 min)

/**
 * @param {number} x
 * @param {number} y
 * @param {number[][]} points
 * @return {number}
 */

let nearestValidPoint = function (x, y, points) {
    let minIndex = -1
    let minDist = 10000

    for (let i in points) {
        let point = points[i]

        if (isValid(x, y, point)) {
            let manDist = manhattanDist(x, y, point[0], point[1])

            if (manDist < minDist) {
                minDist = manDist
                minIndex = i
            }
        }
    }

    return minIndex
}

function manhattanDist(x1, y1, x2, y2) {
    return Math.abs(x1 - x2) + Math.abs(y1 - y2)
}

function isValid(x, y, point) {
    return (x === point[0] || y === point[1]) ? true : false
}
