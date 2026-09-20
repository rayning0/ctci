# https://leetcode.com/problems/merge-k-sorted-lists/description/
# https://neetcode.io/solutions/merge-k-sorted-lists
# Min Heap

import heapq
from list_helper import ListNode, makeList, printList

# 1. Min Heap. Best for interview!
# For each non-empty list, push its head into min heap.
# Pop smallest node from heap.
# Attach it to curr.next and move curr forward.
# If this node has a next node, push that next node onto heap.
# When heap is empty, you're done. All nodes are now merged in sorted order.

# Time: O(n log k), Space: O(k)

# Add HeapNode specifically to pass LeetCode solution, since in LC we can't add "__lt__" function to ListNode.
# "__lt__" function is only to show heapq how to compare 2 Nodes (node a < node b) in a heap.
class HeapNode:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

# Otherwise, if I can change ListNode in LeetCode, I'd do this instead:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#     def __lt__(self, other):
#         return self.val < other.val

class Solution:
    def mergeKLists(lists: list[ListNode | None]) -> ListNode | None:
        dummy = curr = ListNode()
        heap = []

        # Push head (node #1) from each non-empty list onto min heap.
        # (Each head is only a pointer to node #1 of each list. It's NOT the whole list!)
        for head in lists:
            if head:
                heapq.heappush(heap, HeapNode(head))

        # Heap always has only ONE CURRENT NODE from each list!
        # Heap stores REFERENCES (pointers) to ListNode objects, not copies of whole lists.
        while heap:
            # Pop smallest node from heap. Link it to curr.next.
            heap_node = heapq.heappop(heap) # heappop outputs HeapNode
            curr.next = heap_node.node      # HeapNode.node = ListNode
            curr = curr.next
            if curr.next:
                heapq.heappush(heap, HeapNode(curr.next))

        return dummy.next

# 2. Merge Lists 1 by 1. Easiest to remember.
# Time: O(n * k), Space: O(1)
# k = # of linked lists, n = total nodes across all lists
def mergeKLists(lists: list[ListNode | None]) -> ListNode | None:
    if not lists:
        return None

    for i in range(1, len(lists)):
        lists[i] = merge2Lists(lists[i - 1], lists[i])

    return lists[-1]

def merge2Lists(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    head = curr = ListNode()

    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    curr.next = l1 or l2

    return head.next

# 3. Divide and Conquer (Recursion). Merge sort on linked lists.
# Time: O(n log k), Space: O(log k)
# def mergeKLists(lists: list[ListNode | None]) -> ListNode | None:
#     if not lists:
#         return None

#     return divide(lists, 0, len(lists) - 1)

# def divide(lists, l, r):
#     if l == r:
#         return lists[l]

#     mid = (l + r) // 2
#     left = divide(lists, l, mid)
#     right = divide(lists, mid + 1, r)

#     return merge2Lists(left, right)

# 4. Divide and Conquer (Iteration). Repeatedly merge 2 lists at a time, shrinking k lists down to 1.
# Time: O(n log k), Space: O(log k)
# def mergeKLists(lists: list[ListNode | None]) -> ListNode | None:
#     if not lists:
#         return None

#     while len(lists) > 1:
#         merged_lists = []
#         for i in range(0, len(lists), 2):   # increment by 2
#             l1 = lists[i]
#             l2 = lists[i + 1] if (i + 1) < len(lists) else None
#             merged_lists.append(merge2Lists(l1, l2))
#         lists = merged_lists

#     return lists[0]

if __name__ == "__main__":
    l1 = makeList([1,4,5])
    l2 = makeList([1,3,4])
    l3 = makeList([2,6])
    assert printList(mergeKLists([l1, l2, l3])) == '1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6 -> None'

    assert mergeKLists([]) == None
    assert mergeKLists([None]) == None
    print("All tests passed!")
