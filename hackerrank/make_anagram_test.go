package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

// https://www.hackerrank.com/challenges/ctci-making-anagrams

// Given two strings that may or not be of same length, find
// min # of character deletions needed to make both into anagrams.
// Any characters can be deleted from either string.

// Answer with maps:
func makeAnagram(a string, b string) int32 {
	var total int32 = 0
	freqA := make(map[rune]int32)
	freqB := make(map[rune]int32)
	chars := make(map[rune]bool)

	for _, char := range a {
		freqA[char]++
		chars[char] = true
	}
	// r := rune('s'), string(r) => "s"

	for _, char := range b {
		freqB[char]++
		chars[char] = true
	}

	for char := range chars {
		if freqA[char] > freqB[char] {
			total += freqA[char] - freqB[char]
		} else {
			total += freqB[char] - freqA[char]
		}
	}

	return total
}

// Answer with arrays:
// func makeAnagram(a string, b string) int32 {
// 	var total int32 = 0
// 	var freqA [26]int32
// 	var freqB [26]int32
// 	chars := make(map[rune]bool)

// 	// r := rune('s'), string(r) => "s"

// 	for _, char := range a {
// 		i := charToIndex(char)
// 		freqA[i]++
// 		chars[char] = true
// 	}

// 	for _, char := range b {
// 		i := charToIndex(char)
// 		freqB[i]++
// 		chars[char] = true
// 	}

// 	for char := range chars {
// 		i := charToIndex(char)
// 		if freqA[i] > freqB[i] {
// 			total += freqA[i] - freqB[i]
// 		} else {
// 			total += freqB[i] - freqA[i]
// 		}
// 	}

// 	return total
// }

// 'a' = 0, 'b' = 1,...'z' = 25
// func charToIndex(char rune) int {
// 	return int(rune(char) - 97)
// }

func TestAnagram(t *testing.T) {
	tests := []struct {
		a        string
		b        string
		expected int32
	}{
		{"cde", "dcf", 2},
		{"cde", "abc", 4},
		{"mississippi", "assistant", 12},
	}
	for _, test := range tests {
		assert.Equal(t, test.expected, makeAnagram(test.a, test.b))
	}
}
