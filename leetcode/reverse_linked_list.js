// My iterative LeetCode answer to "206. Reverse Linked List":
// https://leetcode.com/submissions/detail/646430195/
// Runtime: 89 ms (beats 58% of JS submissions). Memory: 44.1 MB (beats 31% of JS submissions)
// See this for your other linked list functions, in detail: https://github.com/rayning0/ctci/blob/master/data_structures/linked_list.test.js#L237

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
var reverseList = function(head) {
    var prev = null;
    var current = head;

    while(current) {
        next = current.next
        current.next = prev;
        prev = current;
        current = next;
    }

    return prev;
};
