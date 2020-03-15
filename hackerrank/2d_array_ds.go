// https://www.hackerrank.com/challenges/2d-array/problem

func hourglassSum(arr [][]int32) int32 {
    var maxsum int32 = -63 // lowest a sum can go, with seven -9's
    var sum int32 = -63
    for row := 0; row <= len(arr) - 3; row++ {
        for col := 0; col <= len(arr[0]) - 3; col++ {
            sum = arr[row][col] + arr[row][col+1] + arr[row][col+2] +
                  arr[row+1][col+1] +
                  arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]
            if sum > maxsum {
                maxsum = sum
            }
        }
    }

    return maxsum
}
