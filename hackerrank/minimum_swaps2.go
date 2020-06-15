// https://www.hackerrank.com/challenges/minimum-swaps-2/problem
// Best video explanation: https://www.youtube.com/watch?v=JrzIgYS3SqM

// 1 => 2 => 4 => 3 => 1

// Complete the minimumSwaps function below.
func minimumSwaps(arr []int32) int32 {
    ans := int32(0)
    visited := make(map[int32]bool)

    for i := int32(0); i < int32(len(arr)); i++ {
        if visited[i] || arr[i] == int32(i + 1) {
            visited[i] = true
            continue
        }
        cycleLength := int32(1)
        nextIndex := arr[i] - 1

        for nextIndex != i {
            visited[nextIndex] = true
            cycleLength += 1
            nextIndex = arr[nextIndex] - 1
        }
        ans += cycleLength - 1
    }
    return ans
}
