# https://leetcode.com/problems/copy-list-with-random-pointer/description/
# https://neetcode.io/problems/copy-linked-list-with-random-pointer/solution
# Linked List: Random Pointers (2-Pass Hashmap)

from list_helper import Node, makeList, printList

# 1. 2-pass Hashmap. Easy to remember for interview.
# Time: O(n), Space: O(n)
def copyRandomList(head: Node | None) -> Node | None:
    if head is None:
        return None

    curr = head
    ndict = {}  # Node dictionary: key = original node, value = copied node

    # Pass 1: Make copy of each node. Don't yet set "next" or "random" in copied nodes.
    while curr:
        # print(
        #     f"Node={curr.val}, "
        #     f"next={curr.next.val if curr.next else None}, "
        #     f"random={curr.random.val if curr.random else None}"
        # )
        ndict[curr] = Node(curr.val, None, None)
        curr = curr.next

    curr = head

    # Pass 2: Set "next" and "random" for each copied node to their corresponding copied nodes.
    # Do not point them to original nodes.
    while curr:
        copy = ndict[curr]
        copy.next = ndict[curr.next] if curr.next else None
        copy.random = ndict[curr.random] if curr.random else None
        # print(
        #     f"Node={copy.val}, "
        #     f"next={copy.next.val if copy.next else None}, "
        #     f"random={copy.random.val if copy.random else None}"
        # )
        curr = curr.next

    return ndict[head]  # head of copied node list

# if __name__ == "__main__":
#  print("All tests passed!")

# Ex: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]

# print(index, id(curr), curr.val, id(curr.next), id(curr.random)) shows Object IDs:

# 0 140033789854448 7  140033789839312 10605280
# 1 140033789839312 13 140033789843152 140033789854448
# 2 140033789843152 11 140033789952080 140033789952992
# 3 140033789952080 10 140033789952992 140033789843152
# 4 140033789952992 1  10605280        140033789854448

# print(
#     f"Index={index}, "
#     f"Node={curr.val}, "
#     f"next={curr.next.val if curr.next else None}, "
#     f"random={curr.random.val if curr.random else None}"
# )

# Index=0, Node=7, next=13, random=None
# Index=1, Node=13, next=11, random=7
# Index=2, Node=11, next=10, random=1
# Index=3, Node=10, next=1, random=11
# Index=4, Node=1, next=None, random=7

# Index=0, Node=7, next=13, random=None
# Index=1, Node=13, next=11, random=7
# Index=2, Node=11, next=10, random=1
# Index=3, Node=10, next=1, random=11
# Index=4, Node=1, next=None, random=7
__________________
2. Space Optimized. Too complex. Not worth studying.
Time: O(n), Space: O(1)

This soluion temporarily interleaves copied nodes with their original nodes, uses those interleaved nodes to assign the random pointers, and then separates the 2 lists again. My primary solution uses a hash map because it's much simpler and less error-prone.

The interweaving O(1) solution is brilliant, but relies on a trick:
A → A' → B → B' → C → C'
