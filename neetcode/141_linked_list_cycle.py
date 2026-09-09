# https://leetcode.com/problems/linked-list-cycle/
# https://neetcode.io/solutions/linked-list-cycle
# Linked List: Fast + Slow Pointers

# fast pointer moves 2 steps each time
# slow pointer moves 1 step each time

from list_helper import ListNode, makeCycleList

# 1. Fast + Slow Pointers (Floyd's Cycle Detection)
# Time: O(n), Space: O(1)
def hasCycle(head: ListNode | None) -> bool:
    fast = slow = head

    # only check fast pointer is not None, since it's ahead of slow
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True

    return False

# 2. Hashset: Easy to remember.
# Time: O(n), Space: O(n)
def hasCycle(head: ListNode | None) -> bool:
    seen = set()
    curr = head

    while curr:
        if curr in seen:
            return True
        seen.add(curr)
        curr = curr.next

    return False

# When add each ListNode "curr" to "seen" set, what is added to "seen"?

# The set stores memory address (reference) of each node object, NOT its integer value.
#   - Python stores references to the ListNode objects in memory.
#   - If node is at memory address 0x10f831200, the set stores that exact identifier.
#   - It looks like collection of object references inside set: {<__main__.ListNode object at 0x...>, <__main__.ListNode object at 0x...>}.
#
# Why This Works
# - Python uses node object's memory ID for its hash value (hash(curr)).
# - When checking if "curr" in "seen", Python checks if that memory address already in set.
# - 2 different nodes with same .val (ex: 2 nodes holding number 3) have different memory addresses.
# Python treats each as distinct object. If set has 1st "3" in it, when we see 2nd "3", "if curr in seen == False".

if __name__ == "__main__":
    assert hasCycle(makeCycleList([3, 2, 0, -4], 1)) is True
    assert hasCycle(makeCycleList([1, 2], 0)) is True
    assert hasCycle(makeCycleList([1, 2], -1)) is False
    assert hasCycle(makeCycleList([1], -1)) is False
    assert hasCycle(makeCycleList([1, 2, 3, 4, 3], 1)) is True
    assert hasCycle(makeCycleList([1, 2, 3, 4, 3], -1)) is False

    print("All tests passed!")
