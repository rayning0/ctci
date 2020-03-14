// https://www.hackerrank.com/challenges/ctci-ransom-note/problem
package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
    "strconv"
    "strings"
)

// checkMagazine has the following parameters:
// magazine: an array of strings, each a word in the magazine
// note: an array of strings, each a word in the ransom note

// Complete the checkMagazine function below.
func checkMagazine(magazine []string, note []string) {
    fMag := make(map[string]int)
    for _, word := range magazine {
        fMag[word]++
    }
    for _, word := range note {
        if fMag[word] > 0 {
            fMag[word]--
        } else {
            fmt.Println("No")
            return
        }
    }

    fmt.Println("Yes")
}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 1024 * 1024)

    mn := strings.Split(readLine(reader), " ")

    mTemp, err := strconv.ParseInt(mn[0], 10, 64)
    checkError(err)
    m := int32(mTemp)

    nTemp, err := strconv.ParseInt(mn[1], 10, 64)
    checkError(err)
    n := int32(nTemp)

    magazineTemp := strings.Split(readLine(reader), " ")

    var magazine []string

    for i := 0; i < int(m); i++ {
        magazineItem := magazineTemp[i]
        magazine = append(magazine, magazineItem)
    }

    noteTemp := strings.Split(readLine(reader), " ")

    var note []string

    for i := 0; i < int(n); i++ {
        noteItem := noteTemp[i]
        note = append(note, noteItem)
    }

    checkMagazine(magazine, note)
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
