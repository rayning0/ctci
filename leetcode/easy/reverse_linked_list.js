// https://leetcode.com/problems/reverse-linked-list/
// See all other linked list functions in detail: https://github.com/rayning0/ctci/blob/master/data_structures/linked_list.test.js
// 3 companies asking this: Microsoft, Bloomberg, Amazon

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */

// iterative
// https://leetcode.com/submissions/detail/654329569/
// Runtime: 107 ms (beats 36% of JS submissions). Memory: 44.6 MB (beats 11% of JS submissions)
// O(n) time, O(1) space
// Time to write code: 54 secs
let reverseList = function(head) {
    let [prev, curr] = [null, head]

    while (curr) {
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    }
    return prev
}

// recursive
// https://leetcode.com/submissions/detail/654344962/
// O(n) time, O(1) space
// Finding Big O for recursive functions: https://stackoverflow.com/questions/13467674/determining-complexity-for-recursive-functions-big-o-notation
// Time to write code: 57 secs
let reverseList = function(curr) {
    if (curr === null || curr.next === null) return curr

    let newHead = reverseList(curr.next)
    curr.next.next = curr // means next.next = previous, points back to curr
    curr.next = null

    return newHead
}
