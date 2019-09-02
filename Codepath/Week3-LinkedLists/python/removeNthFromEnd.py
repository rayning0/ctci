# Problem: Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
# Input: 1->2->3->4->5, n = 2
# Output: 1->2->3->5
#
# Explanation: We remove the second node from the end, the node with value 4
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
     dummy = ListNode(0)
     dummy.next = head
     first = dummy
     second = dummy
     # Advances first pointer so that the gap between first and second is n nodes apart
     for i in range(n+1):
         first = first.next
     # Move first to the end, maintaining the gap
     while (first != None):
         first = first.next
         second = second.next
     second.next = second.next.next
     return dummy.next
