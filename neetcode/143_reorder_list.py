# https://leetcode.com/problems/reorder-list/description/
# https://neetcode.io/solutions/reorder-list
# Linked List: 2 Pointers, Reverse List, then Merge List

# Don't return anything. Modify in-place.

from list_helper import ListNode, makeList, printList

# Time: O(n), Space: O(1)
def reorderList(head: Optional[ListNode]) -> None:
    print(f"Start: {printList(head)}")

    # 1. Find middle of list (with slow/fast pointers):
    # Since fast moves twice the speed of slow, by end of list, slow is in middle.
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    print(f"1. Middle of list: {slow.val}")

    # 2. Reverse 2nd half of list:
    prev = None
    curr = slow

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    print(f"2. Reverse 2nd half. New 2nd half points {slow.val} <- {prev.val}.")

    # 3. With 2 pointers, merge 1st + 2nd halves of list
    p1, p2 = head, prev
    print(f"3. From opposite ends, {p1.val} and {p2.val}, merge 1st + 2nd halves.")

    while p2.next:
        next = p1.next                  # store next p1 node
        p1.next = p2                    # link 1st half node p1 to 2nd half node p2
        print(f"{p1.val} -> {p2.val}")
        p1 = next                       # move p1 forward

        next = p2.next                  # store next p2 node
        p2.next = p1                    # link 2nd half node p2 to 1st half node p1
        print(f"{p2.val} -> {p1.val}")
        p2 = next                       # move p2 forward

    print(f"End:   {printList(head)}\n")

# Why "while p2.next:"? Not "while p2:" or "while p1:"?
# 1. Length of right half is always <= left of left half
# 2. Since we reverse right half starting at "slow", the middle node belongs to both halves.
# 3. Last node of reversed right half is ALWAYS same node as end of left half. Don't want to add last node in twice.

# Splitting [1,2,3,4,5] gives:
# Left:   1 → 2 → 3
# Right:  5 → 4 → 3

# Splitting [1,2,3,4] gives:
# Left:   1 → 2 → 3
# Right:  4 → 3

# Both halves end with node 3, already added in left half. Don't want to add 3 on right side.
# Plus length of right half <= length of left half. So right half ends earlier than left.

# For "Right:  5 → 4 → 3", "while p2.next:" only runs for nodes 5 and 4.
# When p2 = 3, p2.next = None, so "while p2.next = while None" and stops.


if __name__ == "__main__":
    l = makeList([1,2,3,4])
    reorderList(l)
    assert printList(l) == '1 -> 4 -> 2 -> 3 -> None'

    l = makeList([1,2,3,4,5])
    reorderList(l)
    assert printList(l) == '1 -> 5 -> 2 -> 4 -> 3 -> None'

    print("All tests passed!")
