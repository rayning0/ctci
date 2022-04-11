// https://leetcode.com/problems/rotate-array/
// https://leetcode.com/submissions/detail/678062438/
// 3 companies asking it: Amazon, Microsoft, Facebook
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums IN-PLACE instead!!!
 */
// Solution 1:
// SIMPLEST ANSWER!!!
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

// Solution 2:
// O(n) time, O(n) space
let rotate = function(nums, k) {
    const len = nums.length
    let destination = whereItGoes(0, k, len)
    let sliceindex = len - destination

    const left = nums.slice(sliceindex)
    nums.unshift(...left)
    nums.splice(len)
}

// Solution 3. Do 3 reverses.
// O(n) time, O(1) space
let rotate = function(nums, k) {
    nums.reverse()
    k = k % nums.length
    rev(nums, 0, k - 1)
    rev(nums, k, nums.length - 1)
}

function rev(nums, start, end) {
    while (start < end) {
        let temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start++
        end--
    }
}
