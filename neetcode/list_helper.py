class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

def printList(head: ListNode | None) -> str:
    """Converts linked list into a readable string format."""
    curr = head
    output = ''
    while curr:
        output += str(curr.val) + ' -> '
        curr = curr.next
    output += 'None'

    return output

def makeList(vals: list[int]) -> ListNode | None:
    """Creates linked list from list of integers and returns its head."""
    node = next = None
    for val in reversed(vals):
        node = ListNode(val, next)
        next = node

    return node

def makeCycleList(vals: list[int], pos: int) -> ListNode | None:
    """Creates linked list whose tail points to node at index `pos`.

    `pos` is zero-based, as in LeetCode's linked-list problems.  If pos == -1, list does not have a cycle.
    """
    if not vals:
        return None
    if pos < -1 or pos >= len(vals):
        raise ValueError("pos must be -1 or a valid index in vals")

    # 1. Make linked list without cycle
    head = makeList(vals)

    cycle_start = head
    for _ in range(pos):
        cycle_start = cycle_start.next

    tail = head
    while tail.next is not None:
        tail = tail.next

    if pos >= 0:
        # 2. Point tail of list to index pos of list, where cycle starts
        tail.next = cycle_start

    return head

# Ex: head = [3,2,0,-4], pos = 1
# 1. Make linked list without cycle
# l = makeList([3,2,0,-4])

# 2. Point tail of list to index pos of list, where cycle starts
# l.next.next.next.next = l.next
