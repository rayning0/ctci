# https://leetcode.com/problems/merge-two-sorted-lists/description/
# Best video animation: https://www.youtube.com/watch?v=E5XXiY6QnAs
# https://neetcode.io/solutions/merge-two-sorted-lists
# 2 Pointers. Modify list in place.

from list_helper import ListNode, makeList, printList

# Keep pointer (curr) to current end of the merged list, and at each step choose the smaller
# head node from list1 or list2. Since lists already sorted, smaller head must
# come next in merged list. Attach that node, move the pointer forward, and continue
# till 1 list is empty. Finally, attach remaining nodes from the non-empty list.
# Using a "head" node makes handling head of final merged list simple and clean.

# 1. Iterative. 2 Pointers. Make dummy node.
# Time: O(n + m), Space: O(1)
def mergeTwoLists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    head = curr = ListNode()

    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next

    curr.next = list1 or list2

    return head.next

# 2. Recursive
# Time: O(n + m), Space: O(n + m)
def mergeTwoLists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    # base case
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.val < list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2

if __name__ == "__main__":
    l1, l2 = makeList([1,2,4]), makeList([1,3,4])
    print(printList(l1))
    print(printList(l2))
    assert printList(mergeTwoLists(l1, l2)) == '1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None'

    l1, l2 = makeList([1,2,4]), makeList([1,3,5])
    print(printList(l1))
    print(printList(l2))
    assert printList(mergeTwoLists(l1, l2)) == '1 -> 1 -> 2 -> 3 -> 4 -> 5 -> None'

    l1, l2 = makeList([]), makeList([])
    print(printList(l1))
    print(printList(l2))
    assert printList(mergeTwoLists(l1, l2)) == 'None'

    l1, l2 = makeList([]), makeList([0])
    print(printList(l1))
    print(printList(l2))
    assert printList(mergeTwoLists(l1, l2)) == '0 -> None'
    print("All tests passed!")
_____________________________________________________________________
Iterative Example:

list1: 1 ➔ 2 ➔ 4
list2: 1 ➔ 3 ➔ 4

head, curr
   ▼
[Dummy (0)] ➔ None

list1 ➔ (1) ➔ (2) ➔ (4) ➔ None
list2 ➔ (1) ➔ (3) ➔ (4) ➔ None


Since list1.val < list2.val (1 < 1) is False. (Go to else block).
Execution:
- Connect curr to list2.
- Advance list2 to 3.
- Advance curr to 1.

head
  ▼
[Dummy (0)] ➔ (1) ➔ (3) ➔ (4) ➔ None
               ▲
              curr

list1 ➔ (1) ➔ (2) ➔ (4) ➔ None
list2 ─────────► (3) ➔ (4) ➔ None

Since list1.val < list2.val (1 < 3) is True.
Execution:
- Connect curr to list1.
- Advance list1 to 2.
- Advance curr to 1.

head
  ▼
[Dummy (0)] ➔ (1) ➔ (1) ➔ (2) ➔ (4) ➔ None
                     ▲
                    curr

list1 ───────────────► (2) ➔ (4) ➔ None
list2 ➔ (3) ➔ (4) ➔ None

Since list1.val < list2.val (2 < 3) is True.
- Connect curr to list1.
- Advance list1 to 4.
- Advance curr to 2.

head
  ▼
[Dummy (0)] ➔ (1) ➔ (1) ➔ (2) ➔ (4) ➔ None
                           ▲
                          curr

list1 ───────────────────────────► (4) ➔ None
list2 ➔ (3) ➔ (4) ➔ None

Since list1.val < list2.val (4 < 3) is False.
- Connect curr to list2.
- Advance list2 to 4.
- Advance curr to 3.

head
  ▼
[Dummy (0)] ➔ (1) ➔ (1) ➔ (2) ➔ (3) ➔ (4) ➔ None
                                 ▲
                                curr

list1 ➔ (4) ➔ None
list2 ─────────────────────────────────► (4) ➔ None


Since list1.val < list2.val (4 < 4) is False.
- Connect curr to list2.
- Advance list2 to None.
- Advance curr to 4.

head
  ▼
[Dummy (0)] ➔ (1) ➔ (1) ➔ (2) ➔ (3) ➔ (4) ➔ None
                                       ▲
                                      curr

list1 ➔ (4) ➔ None
list2 ───────────────────────────────────────► None (Empty!)


The while list1 and list2: loop terminates here because list2 is empty (None).
The Remainder Line: curr.next = list1 or list2
The pointer list1 still points to its remaining Node (4). This line stitches the
remaining node right onto the end of our working sequence in one final move.

head
  ▼
[Dummy (0)] ➔ (1) ➔ (1) ➔ (2) ➔ (3) ➔ (4) ➔ (4) ➔ None
                                             ▲
                                            curr

The function ends with "return head.next".
This entirely bypasses arbitrary [Dummy (0)] and spits out
the cleanly ordered sequence: 1 ➔ 1 ➔ 2 ➔ 3 ➔ 4 ➔ 4.
_____________________________________________________________________
Recursive Example:

list1 = [1 -> 4], list2 = [2 -> 3]

Phase 1: Going Down (Building Call Stack)

Each recursive call pauses execution at a assignment line (listX.next = ...) and passes a smaller sub-problem to the next frame.

Call 1: merge( [1 ➔ 4], [2 ➔ 3] )
    Compare: 1 <= 2 is True. Node (1) is chosen.
    Action: Needs to find its tail, so it calls 1.next = merge( [4], [2 ➔ 3] ).

Call 2: merge( [4], [2 ➔ 3] )
    Compare: 4 <= 2 is False. Node (2) is chosen.
    Action: Needs to find its tail, so it calls 2.next = merge( [4], [3] ).

Call 3: merge( [4], [3] )
    Compare: 4 <= 3 is False. Node (3) is chosen.
    Action: Needs to find its tail, so it calls 3.next = merge( [4], [] ).

Call 4 (Base Case): merge( [4], [] )
    Condition Met: list2 is empty.
    Action: Immediately returns the remainder of list1, which is just node (4).

Phase 2: Coming Up (Unwinding and Linking)

Now the stack pops backwards. As each function frame resumes, it returns its chosen node up to the caller, which links its .next pointer to it.

[Base Case Ret]  Returns Node (4)
                       │
                       ▼
[Call 3 Resumes] Sets  (3).next = (4)  ──▶  Result: 3 ➔ 4
                       │                    Returns Node (3)
                       ▼
[Call 2 Resumes] Sets  (2).next = (3)  ──▶  Result: 2 ➔ 3 ➔ 4
                       │                    Returns Node (2)
                       ▼
[Call 1 Resumes] Sets  (1).next = (2)  ──▶  Result: 1 ➔ 2 ➔ 3 ➔ 4
                                            Returns Node (1) (Final Head)

Tree/Stack Diagram of Calls

Visual map showing flow down into base cases and how values are cleanly threaded on the way back out:

merge(1➔4, 2➔3) ──[ 1 <= 2 ]──▶ list1.next = merge(4, 2➔3) ──── (Returns Node 1)
                                                 │                   ▲
                                             [ 4 > 2 ]               │ (Links 1 ➔ 2)
                                                 ▼                   │
                                            list2.next = merge(4, 3) ─── (Returns Node 2)
                                                             │               ▲
                                                         [ 4 > 3 ]           │ (Links 2 ➔ 3)
                                                             ▼               │
                                                        list2.next = merge(4, None)
                                                                         │   ▲
                                                                     [Base Case] (Links 3 ➔ 4)
                                                                         ▼   │
                                                                   Returns Node 4
