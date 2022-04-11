// https://leetcode.com/problems/contains-duplicate/
// https://leetcode.com/submissions/detail/678259398/
// Time to code: 5:50 min
/**
 * @param {number[]} nums
 * @return {boolean}
 */
// O(n) time, O(n) space
let containsDuplicate = function (nums) {
    let hash = {}
    for (let num of nums) {
        if (hash[num]) {
            return true
        } else {
            hash[num] = true
        }
    }
    return false
}
