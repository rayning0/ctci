/* Given a 2D matrix, print all elements of the given matrix in diagonal order.
For example, given this 5 X 4 matrix:

    1     2     3     4
    5     6     7     8
    9    10    11    12
   13    14    15    16
   17    18    19    20
Diagonal printing of the above matrix is

    1
    5     2
    9     6     3
   13    10     7     4
   17    14    11     8
   18    15    12
   19    16
   20

  Coordinates:
  0,0
  1,0 0,1
  2,0 1,1 0,2
  3,0 2,1 1,2 0,3
  4,0 3,1 2,2 1,3
  4,1 3,2 2,3
  4,2 3,3
  4,3
*/

package main

import "fmt"

func main() {
	a := [][]int{
		{1, 2, 3, 4},
		{5, 6, 7, 8},
		{9, 10, 11, 12},
		{13, 14, 15, 16},
		{17, 18, 19, 20},
	}
	diag(a)
}

func diag(a [][]int) {
	height, width := len(a), len(a[0])
	line := []int{}

	for row := 0; row < height-1; row++ {
		r := row
		for col := 0; col <= row; col++ {
			line = append(line, a[r][col])
			r -= 1
		}
		fmt.Println(line)
		line = []int{}
	}

	for row := 0; row < height-1; row++ {
		r := height - 1
		for col := row; col < width; col++ {
			line = append(line, a[r][col])
			r -= 1
		}
		fmt.Println(line)
		line = []int{}
	}
}

// Output:
// [1]
// [5 2]
// [9 6 3]
// [13 10 7 4]
// [17 14 11 8]
// [18 15 12]
// [19 16]
// [20]
