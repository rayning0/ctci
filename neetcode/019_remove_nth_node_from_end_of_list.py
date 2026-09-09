# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# https://neetcode.io/solutions/remove-nth-node-from-end-of-list

from list_helper import ListNode, makeList, printList

# 1. 2 Pointers: 1-Pass.
# How to keep 2 pointers n nodes apart?

# Time: O(n), Space: O(1)
def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode()
    dummy.next = head
    p1, p2 = dummy, dummy

    # Move p2 forward n+1 nodes, so when p2 reaches None in "while" loop,
    # p1 points to 1 node BEFORE target node.
    for _ in range(n + 1):
        p2 = p2.next

    # Move both p1 and p2 the same amount.
    # Move p2 to None (end of list).
    # Move p1 to 1 node BEFORE target!
    while p2:
        p1 = p1.next
        p2 = p2.next

    p1.next = p1.next.next  # Link p1 to 1 node after target!
    return dummy.next

# Ex: head = '1 -> 2 -> 3 -> 4 -> 5 -> None', n = 2
# p1 = p2 = dummy -> '1 -> 2 -> 3 -> 4 -> 5 -> None'

# After moving p2 forward n+1 = 3 nodes:
# p1 = dummy -> '1 -> 2 -> 3 -> 4 -> 5 -> None'
#                              p2

# After "while p2" loop to end of list:
# dummy -> '1 -> 2 -> 3 -> 4          -> 5 -> None'
#                         p1   target              p2

# After p1.next = p1.next.next (Link p1 to 1 node after target):
# dummy -> '1 -> 2 -> 3 -> 5 -> None'
#                         p1          p2

# dummy.next = '1 -> 2 -> 3 -> 5 -> None'

# 2. Iteration: 2-Pass.
# Time: O(n), Space: O(1)
def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy  = ListNode()
    dummy.next = head

    # find list length
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next

    curr = dummy                # Start 1 node before head
    for _ in range(length - n): # Move to node 1 BEFORE target node!
        curr = curr.next
    curr.next = curr.next.next  # Link 1 node before target to 1 node after target!

    return dummy.next

if __name__ == "__main__":
    assert printList(removeNthFromEnd(makeList([1,2,3,4,5]), 2)) == '1 -> 2 -> 3 -> 5 -> None'
    assert printList(removeNthFromEnd(makeList([1]), 1)) == 'None'
    assert printList(removeNthFromEnd(makeList([1,2]), 1)) == '1 -> None'
    assert printList(removeNthFromEnd(makeList([1,2]), 2)) == '2 -> None'

    print("All tests passed!")
