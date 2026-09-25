# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# https://neetcode.io/solutions/maximum-depth-of-binary-tree
# DFS (Depth-First Search)

# For each node:
# 1. Find depth of its left and right children.
# 2. Return 1 + max(left depth, right depth)

from tree_helper import TreeNode, printTree, makeTree
from collections import deque

# 1. DFS (Recursion): Ask each child for their depths.
# Time: O(n) <--- must visit all nodes
# Space: O(h), h = tree height.
# - Best case (balanced tree): O(log n). h = log n. Each node has 2 children.
# - Worse case (skewed tree):  O(n).     h = n. Each node has only 1 child.
def maxDepth(root: TreeNode | None) -> int:
    if not root:
        return 0

    left = maxDepth(root.left)
    right = maxDepth(root.right)

    return 1 + max(left, right)

# 2. BFS: process 1 tree level at a time
# While queue exists:
#   Loop through len(queue) = size of each tree level
#       For each node, append its child to queue
#   Depth += 1

# Time: O(n), Space: O(n)
def maxDepth(root: TreeNode | None) -> int:
    if not root:
        return 0

    depth = 0
    q = deque([root])   # deque() always takes iterable [] input. Can't use deque(root)!

    while q:
        level_size = len(q)
        for _ in range(level_size):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        depth += 1

    return depth

if __name__ == "__main__":
    tree = makeTree([3,9,20,None,None,15,7])
    printTree(tree)
    assert maxDepth(tree) == 3

    tree = makeTree([1,None,2])
    assert maxDepth(tree) == 2

    tree = makeTree([1,2,3,None,None,4])
    assert maxDepth(tree) == 3

    tree = makeTree([])
    assert maxDepth(tree) == 0
    print("All tests passed!")

# Q: For balanced tree, why is height = log n?
# Each level doubles the capacity. A tree of height h holds up to 2^h nodes. To fit n nodes, you need h = log₂(n) levels — just like you need log₂(n) bits to represent n values.

# A balanced binary tree doubles number of nodes at each level:
# Level 0:        1         → 1 node    (2⁰)
# Level 1:       / \        → 2 nodes   (2¹)
# Level 2:      / \ / \     → 4 nodes   (2²)
# Level 3:     /\ /\ /\ /\  → 8 nodes   (2³)
# ...
# Level h:                        → 2ʰ nodes

# n = 1 + 2 + 4 + 8 + ... + 2ʰ
# n = 2^(h+1) - 1
# n ≈ 2^(h+1)
# log₂(n) ≈ h + 1
# h ≈ log₂(n) - 1 = O(log n)

# This is also why binary search has O(log n) space complexity if recursive.

# Each time a function calls itself (RECURSION), Python allocates memory on the call stack to store that call's local variables and return address.

# For this tree:
#     1
#    / \
#   2   3
#  /
# 4
# Its call stack grows like this:
# ┌─────────────────────┐
# │ maxDepth(1)         │  ← frame 1: stores root=1, left=?, right=?
# │   calls maxDepth(2) │
# ├─────────────────────┤
# │ maxDepth(2)         │  ← frame 2: stores root=2, left=?, right=?
# │   calls maxDepth(4) │
# ├─────────────────────┤
# │ maxDepth(4)         │  ← frame 3: stores root=4, left=?, right=?
# │   calls maxDepth(N) │
# ├─────────────────────┤
# │ maxDepth(None) → 0  │  ← frame 4: base case, returns immediately
# └─────────────────────┘

# At this point, 4 frames are on the stack = height of the tree + 1.

# - Each active (not yet returned) recursive call occupies 1 stack frame.
# - Stack frames are only freed when the function returns.
# - The maximum number of frames alive at the same time equals the longest path from root to leaf — which is exactly the height h.

# Frames on stack at deepest point:

# Path: 1 → 2 → 4 → None
#        ↓    ↓    ↓    ↓
#      [f1] [f2] [f3] [f4]  → 4 frames = h + 1 = O(h)

# Q: What's a "call stack" and "stack frame"?

# Call Stack
# Think of it like a stack of plates. When your program runs, Python maintains a to-do list of functions that are currently executing. This list is the call stack.

# When a function is called → push a plate on top
# When a function returns → pop the top plate off
# It follows LIFO (Last In, First Out) — the most recently called function finishes first.

# Calling maxDepth(1) → maxDepth(2) → maxDepth(None):

#   push       push       push
#  ┌────┐    ┌────┐    ┌────┐
#  │ f1 │ →  │ f2 │ →  │ f3 │    ← call stack grows upward
#  └────┘    │ f1 │    │ f2 │
#            └────┘    │ f1 │
#                      └────┘

# Now maxDepth(None) returns 0:

#   pop
#  ┌────┐
#  │ f2 │    ← f3 is removed, execution resumes in f2
#  │ f1 │
#  └────┘

# Stack Frame
# Each "plate" on the stack is a stack frame. It's a small block of memory that stores everything Python needs to resume that function after the called function returns:

# ┌──────────────────────────────┐
# │  Stack Frame for maxDepth(2) │
# │                              │
# │  • root = 2                  │  ← local variables
# │  • left = ? (waiting)        │
# │  • right = ? (waiting)       │
# │  • return address: line 5    │  ← where to resume after call returns
# │  • caller: maxDepth(1)       │  ← who called me
# └──────────────────────────────┘

# When maxDepth(2) calls maxDepth(4), it pauses and a new frame for maxDepth(4) is pushed on top. When maxDepth(4) returns, its frame is popped, and maxDepth(2) resumes exactly where it left off, using the values saved in its frame.
