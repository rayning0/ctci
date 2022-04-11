// https://leetcode.com/problems/intersection-of-two-arrays-ii/
// https://leetcode.com/submissions/detail/678295919/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
// O(n + m) time, O(min(n, m)) space
// Companies: Amazon, Facebook, Yahoo
// Time to code: 20:41 min

let intersect = function(nums1, nums2) {
    [freq, ans] = [{}, []]

    // force num1 to be smaller array
    if (nums2.length < nums1.length) {
        [nums1, nums2] = [nums2, nums1]
    }

    // frequency hash
    for (let num of nums1) {
        if (freq[num]) {
            freq[num]++
        } else {
            freq[num] = 1
        }
    }

    for (let num of nums2) {
        if (freq[num] > 0) {
            ans.push(num)
            freq[num]--
        }
    }

    return ans
}
