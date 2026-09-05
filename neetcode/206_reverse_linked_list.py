# https://leetcode.com/problems/reverse-linked-list/description/
# https://neetcode.io/solutions/reverse-linked-list

# Use 3 pointers: Prev, Curr, Next.
# Make node's Next point back to its Previous node.
# Move all 3 pointers forward to right 1 step.
# Repeat.

# Singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Iterative with 3 pointers
# Time: O(n), Space: O(1)
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head

    while curr:
        next = curr.next

        # point current node backwards: n1.next = None, n2.next = n1, n3.next = n2, ...
        curr.next = prev

        prev = curr
        curr = next

    return prev

def printList(head):
    curr = head
    output = ''
    while curr:
        output += str(curr.val) + ' -> '
        curr = curr.next
    output += 'None'

    return output

def makeList(vals: list[int]) -> [ListNode]:
    node = next = None
    for val in reversed(vals):
        node = ListNode(val, next)
        next = node

    return node

# Use 3 pointers: Prev, Curr, Next

# Prev    Curr    Next
# None    1 ->    2 -> 3 -> None

# Point Curr back to Prev: curr.next = prev
# None <- 1       2 -> 3 -> None

# Move all 3 pointers forward to right (1 step).
# prev = curr
# curr = next
# next = curr.next

#         Prev    Curr    Next
# None <- 1       2 ->    3 -> None

# Point Curr back to Prev: curr.next = prev
# None <- 1   <-  2       3 -> None

# Move all 3 pointers forward to right.
# prev = curr
# curr = next
# next = curr.next

#                 Prev    Curr    Next
# None <- 1   <-  2       3    -> None

# Point Curr back to Prev: curr.next = prev
# None <- 1   <-  2    <- 3       None

# Move all 3 pointers forward to right.
# prev = curr
# curr = next
# next = curr.next

#                         Prev    Curr
# None <- 1   <-  2    <- 3       None

# New head is at Prev, which we return.

if __name__ == "__main__":
    ex1 = makeList([1,2,3,4,5])
    print(printList(ex1))
    assert printList(reverseList(ex1)) == '5 -> 4 -> 3 -> 2 -> 1 -> None'

    ex2 = makeList([1,2])
    print(printList(ex2))
    assert printList(reverseList(ex2)) == '2 -> 1 -> None'

    ex3 = makeList([])
    print(printList(ex3))
    assert printList(reverseList(ex3)) == 'None'

    ex4 = makeList([0,1,2,3])
    print(printList(ex4))
    assert printList(reverseList(ex4)) == '3 -> 2 -> 1 -> 0 -> None'
    print("All tests passed!")
