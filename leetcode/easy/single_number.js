/**
 * @param {number[]} nums
 * @return {number}
 */
// https://leetcode.com/problems/single-number/
// https://leetcode.com/submissions/detail/678275871/
// Bit manipulation with XOR
// O(n) time, O(1) space
// Companies: Amazon, Microsoft, Bloomberg

// 0 ^ a = a
// a ^ a = 0
// a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b
// So XOR all bits together to find unique number

let singleNumber = function(nums) {
    bitProduct = 0
    for (let num of nums) {
        bitProduct ^= num
    }
    return bitProduct
}

// O(n) time, O(n) space
// Time to code: 3:10 min
let singleNumber = function(nums) {
    freq = {}
    for (let num of nums) {
        if (freq[num]) {
            freq[num]++
        } else {
            freq[num] = 1
        }
    }

    for (let num in freq) {
        if (freq[num] == 1) {
            return num
        }
    }
}
