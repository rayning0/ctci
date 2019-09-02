# Problem: Given a linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Can you do it without taking up extra memory?
#
# Examples:
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
#
# Input: 1->1->1->2->3
# Output: 2->3
def deleteDuplicates(self, head: ListNode) -> ListNode:
    dummyHead = ListNode(0)
    dummyHead.next = head
    prev = dummyHead
    current = head

    while current != None:
        while (current.next != None and
               prev.next.val == current.next.val):
            current = current.next

        if prev.next == current:
            prev = prev.next
        else:
            prev.next = current.next

        current = current.next
    return dummyHead.next
