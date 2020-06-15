package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

// Best explanation: https://www.youtube.com/watch?v=tBFZMaWP0W8
// Complete the countTriplets function below.
func countTriplets(arr []int, r int) int {
	count := 0
	rfreq, lfreq := make(map[int]int), make(map[int]int)
	for _, num := range arr {
		rfreq[num]++
	}

	for i := 0; i < len(arr); i++ {
		mid := arr[i]
		cleft, cright := 0, 0
		rfreq[mid]--
		if mid%r == 0 && lfreq[mid/r] > 0 {
			cleft = lfreq[mid/r]
		}
		if rfreq[mid*r] > 0 {
			cright = rfreq[mid*r]
		}
		count += cleft * cright
		lfreq[mid]++
	}
	return count
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 16*1024*1024)

	nr := strings.Split(strings.TrimSpace(readLine(reader)), " ")

	nTemp, err := strconv.Atoi(nr[0])
	// nTemp, err := strconv.ParseInt(nr[0], 10, 64)
	checkError(err)
	n := int(nTemp)

	r, err := strconv.Atoi(nr[1])
	// r, err := strconv.ParseInt(nr[1], 10, 64)
	checkError(err)

	arrTemp := strings.Split(strings.TrimSpace(readLine(reader)), " ")

	var arr []int

	for i := 0; i < int(n); i++ {
		arrItem, err := strconv.Atoi(arrTemp[i])
		// arrItem, err := strconv.ParseInt(arrTemp[i], 10, 64)
		checkError(err)
		arr = append(arr, arrItem)
	}

	ans := countTriplets(arr, r)

	fmt.Fprintf(writer, "%d\n", ans)

	writer.Flush()
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
