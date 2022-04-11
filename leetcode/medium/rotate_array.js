// https://leetcode.com/problems/rotate-array/
// https://leetcode.com/submissions/detail/678248500/
// 3 companies asking it: Amazon, Microsoft, Facebook
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums IN-PLACE instead!!!
 */

// 1. BEST! O(n) time, O(1) space
let rotate = function(nums, k) {
    nums.reverse()
    k = k % nums.length
    rev(nums, 0, k - 1)
    rev(nums, k, nums.length - 1)
}

function rev(nums, start, end) {
    while (start < end) {
        [nums[start], nums[end]] = [nums[end], nums[start]]
        start++
        end--
    }
}


// 2. Simpler
// O(n) time, O(n) space
let rotate = function(nums, k) {
    let temp = [...nums]
    for (let i = 0; i < nums.length; i++) {
        let dest = whereItGoes(i, k, nums.length)
        nums[dest] = temp[i]
    }
}

function whereItGoes(start, k, length) {
    k = k % length
    if (start + k < length) {
        return start + k
    } else {
        return start + k - length
    }
}

// Simplest, but this FAILS due to new LeetCode case that exceeds time limit
let rotate = function(nums, k) {
    k = k % nums.length
    while (k > 0) {
        nums.unshift(nums.pop())
        k--
    }
}
