# Problem: Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode(0)
    p = head
    p1 = l1
    p2 = l2

    while p1 != None and p2 != None:
        if p1.val < p2.val:
            p.next = p1
            p1 = p1.next
        else:
            p.next = p2
            p2 = p2.next
        p = p.next

    if p1 != None:
        p.next = p1

    if p2 != None:
        p.next = p2

    return head.next
