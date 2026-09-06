# https://leetcode.com/problems/reverse-linked-list/description/
# https://neetcode.io/solutions/reverse-linked-list

# Use 3 pointers: Prev, Curr, Next.
# Make node's Next point back to its Previous node.
# Move all 3 pointers forward to right 1 step.
# Repeat.

# Singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1. Iterative with 3 pointers. Reverse in place.
# Time: O(n), Space: O(1)
def reverseList(head: [ListNode]) -> [ListNode]:
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

# 2. Recursive
# "Ask rest of list (after head) to reverse itself. Then attach head to end of this reversed list."
# Time: O(n), Space: O(n) <-- because 1 recursive call per node
def reverseList(head: [ListNode]) -> [ListNode]:
    # base case: "Stop when we have nothing left to reverse"
    if head is None or head.next is None:
        return head

    new_head = reverseList(head.next) # imagine this magically reverses rest of list
    head.next.next = head             # my child (head.next) points back to me (head)
    head.next = None

    return new_head

# Example: head = 1 → 2 → 3 → 4 → None

# Don't reverse whole list. Say "Hey 2, reverse everything after head."
# head = 1 | recurse(2 -> 3 -> 4 -> None)

# After recursion, both head (1) points to 2 and reversed rest of list also points to 2.
# 1 -> 2 <- 3 <- 4

### new_head = reverseList(head.next) = 4 -> 3 -> 2 -> None

# How to point 2 backwards to 1? We want "2.next = 1"

### head.next.next = head means "my child (head.next) points back to me (head)"
# 1 <- 2 <- 3 <- 4

# Point original head to None, then return new_head:
### head.next = None
# None <- 1 <- 2 <- 3 <- 4 = new_head

# What's base case? "Stop when we have nothing left to reverse"
# 1. Empty list: None
# 2. List with 1 node: head.next = None

# How does recursion unwind?
# reverse(4) returns 4 -> None
# reverse(3) gets 4 -> None, makes + returns 4 -> 3 -> None
# reverse(2) gets 4 -> 3 -> None, makes + returns 4 -> 3 -> 2 -> None
# reverse(1) get 4 -> 3 -> 2 -> None, makes + returns 4 -> 3 -> 2 -> 1 -> None

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
