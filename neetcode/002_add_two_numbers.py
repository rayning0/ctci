# https://leetcode.com/problems/add-two-numbers/description/
# https://neetcode.io/solutions/add-two-numbers
# Linked List. Iterative.

from list_helper import ListNode, makeList, printList

# Time: O(max(m, n)), Space: O(1) auxiliary
def addTwoNumbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    carry = 0
    dummy = curr = ListNode()

    # In "while", use OR, not AND! So if l1 or l2 is shorter list, it keeps looping.
    # Add "carry". If both l1 and l2 finished, we still add the final carry.

    # This "while" statement, plus the 4 if-else statements, handles:
    # 1. Different lengths of l1, l2
    # 2. Leftover carry
    # 3. Answer in 1-pass
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0        # if a list ended, it adds 0
        v2 = l2.val if l2 else 0

        total = v1 + v2 + carry
        carry = total // 10
        digit = total % 10
        curr.next = ListNode(digit)

        # move pointers
        curr = curr.next
        l1 = l1.next if l1 else None    # if pointer is at list end (None), it stays None.
        l2 = l2.next if l2 else None

    return dummy.next

if __name__ == "__main__":
    l1 = makeList([2,4,3])
    l2 = makeList([5,6,4])
    assert printList(addTwoNumbers(l1, l2)) == '7 -> 0 -> 8 -> None'

    l1 = makeList([0])
    l2 = makeList([0])
    assert printList(addTwoNumbers(l1, l2)) == '0 -> None'

    l1 = makeList([9])
    l2 = makeList([9])
    assert printList(addTwoNumbers(l1, l2)) == '8 -> 1 -> None'

    l1 = makeList([9,9,9,9,9,9,9])
    l2 = makeList([9,9,9,9])
    assert printList(addTwoNumbers(l1, l2)) == '8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1 -> None'
    print("All tests passed!")
