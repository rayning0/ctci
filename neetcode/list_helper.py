class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(head: ListNode | None) -> str:
    """Converts a linked list into a readable string format."""
    curr = head
    output = ''
    while curr:
        output += str(curr.val) + ' -> '
        curr = curr.next
    output += 'None'

    return output

def makeList(vals: list[int]) -> ListNode | None:
    """Creates a linked list from a list of integers and returns the head."""
    node = next = None
    for val in reversed(vals):
        node = ListNode(val, next)
        next = node

    return node
