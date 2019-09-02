/*
 * Problem: Given a linked list, remove the n-th node from the end of list and return its head.
 *
 * Example:
 * Input: 1->2->3->4->5, n = 2
 * Output: 1->2->3->5
 *
 * Explanation: We remove the second node from the end, the node with value 4
*/
public ListNode removeNthFromEnd(ListNode head, int n) {
    ListNode dummy = new ListNode(0);
    dummy.next = head;
    ListNode first = dummy;
    ListNode second = dummy;
    // Advances first pointer so that the gap between first and second is n nodes apart
    for (int i = 1; i <= n + 1; i++) {
        first = first.next;
    }
    // Move first to the end, maintaining the gap
    while (first != null) {
        first = first.next;
        second = second.next;
    }
    second.next = second.next.next;
    return dummy.next;
}
