// https://leetcode.com/problems/remove-duplicates-from-sorted-array/
// 3 companies asking this: Facebook, Amazon, Adobe
// Use 2 pointers

// Better Answer:
// https://leetcode.com/submissions/detail/654421102/
// Runtime: 76 ms, faster than 92.27% of JavaScript online submissions for Remove Duplicates from Sorted Array.
// Memory Usage: 44.3 MB, less than 55.52% of JavaScript online submissions for Remove Duplicates from Sorted Array.
// O(n) time, O(1) space
// Time to write code: 1:39 min
let removeDuplicates = function(nums) {
    let [i, insertIndex] = [1, 1]

    while (i < nums.length) {
        if (nums[i] !== nums[i - 1]) {
            nums[insertIndex] = nums[i]
            insertIndex++
        }
        // console.log(`insertIndex: ${insertIndex}, i: ${i}, nums[i]: ${nums[i]}`)
        // console.log(nums)

        i++
    }

    return insertIndex
}

OUTPUT:

insertIndex: 1, i: 1, nums[i]: 0
[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

insertIndex: 2, i: 2, nums[i]: 1
[0, 1, 1, 1, 1, 2, 2, 3, 3, 4]

insertIndex: 2, i: 3, nums[i]: 1
[0, 1, 1, 1, 1, 2, 2, 3, 3, 4]

insertIndex: 2, i: 4, nums[i]: 1
[0, 1, 1, 1, 1, 2, 2, 3, 3, 4]

insertIndex: 3, i: 5, nums[i]: 2
[0, 1, 2, 1, 1, 2, 2, 3, 3, 4]

insertIndex: 3, i: 6, nums[i]: 2
[0, 1, 2, 1, 1, 2, 2, 3, 3, 4]

insertIndex: 4, i: 7, nums[i]: 3
[0, 1, 2, 3, 1, 2, 2, 3, 3, 4]

insertIndex: 4, i: 8, nums[i]: 3
[0, 1, 2, 3, 1, 2, 2, 3, 3, 4]

insertIndex: 5, i: 9, nums[i]: 4
[0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
____________________________________
// First Try:
// https://leetcode.com/submissions/detail/654411753/
// Runtime: 72 ms, beats 95.5% of JS submissions. Memory Usage: 45.7 MB, beats 6.5% of JS submissions
// O(n) time, O(1) space
// Time to write code: 1 hour
/**
 * @param {number[]} nums
 * @return {number}
 */
let removeDuplicates = function(nums) {
    if (nums.length === 1) return 1
    let [k, i, j] = [1, 0, 1]
    let newNum = nums[i]

    while (i < nums.length - 1 && j < nums.length) {
        while (newNum === nums[j]) {
            // nums[j] = '_'
            j++
        }

        newNum = nums[j]
        // console.log(`i: ${i}, firstNum: ${nums[i]}, j: ${j}, newNum: ${newNum}, k: ${k}`)

        if (j < nums.length) {
            nums[i + 1] = newNum
            k++
        }

        // console.log(nums)
        i++
        j++
    }

    return k
}

OUTPUT:

i: 0, firstNum: 0, j: 2, newNum: 1, k: 1
[0, 1, 1, 1, 1, 2, 2, 3, 3, 4]

i: 1, firstNum: 1, j: 5, newNum: 2, k: 2
[0, 1, 2, '_', '_', 2, 2, 3, 3, 4]

i: 2, firstNum: 2, j: 7, newNum: 3, k: 3
[0, 1, 2, 3, '_', 2, '_', 3, 3, 4]

i: 3, firstNum: 3, j: 9, newNum: 4, k: 4
[0, 1, 2, 3, 4, 2, '_', 3, '_', 4]
