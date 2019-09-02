/*
 * Problem: Given a linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Can you do it without taking up extra memory?
 *
 * Examples:
 * Input: 1->2->3->3->4->4->5
 * Output: 1->2->5

 * Input: 1->1->1->2->3
 * Output: 2->3
*/
public ListNode deleteDuplicates(ListNode head) {
    ListNode dummyHead = new ListNode(0);
    dummyHead.next = head;
    ListNode prev = dummyHead;
    ListNode current = head;

    while (current != null)
    {
        while (current.next != null &&
               prev.next.val == current.next.val)
            current = current.next;

        if (prev.next == current)
            prev = prev.next;
        else
            prev.next = current.next;

        current = current.next;
    }
    return dummyHead.next;
}
