# https://leetcode.com/problems/invert-binary-tree/description/
# https://neetcode.io/solutions/invert-binary-tree
# DFS

# For each node:
# 1. Swap children.
# 2. Tell left child to do the same.
# 3. Tell right child to do the same.

from tree_helper import TreeNode, printTree, makeTree
from collections import deque

# 1. DFS
# Time: O(n)
# Space: O(h) <-- O(log n) balanced tree, O(n) worst case tree
def invertTree(root: TreeNode | None) -> TreeNode | None:
    if not root:
        return None

    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)

    return root

# 2. BFS
# While queue exists:
# For each node, swap its children.
# Add its children to queue.

# Time: O(n), Space: O(n)
def invertTree(root: TreeNode | None) -> TreeNode | None:
    if not root:
        return None

    q = deque([root])

    while q:
        node = q.popleft()
        node.left, node.right = node.right, node.left

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return root

if __name__ == "__main__":
    tree = makeTree([4,2,7,1,3,6,9])
    print(printTree(tree))
    assert printTree(invertTree(tree)) == [4,7,2,9,6,3,1]

    tree = makeTree([1,2,3,4,5,6,7])
    print(printTree(tree))
    assert printTree(invertTree(tree)) == [1,3,2,7,6,5,4]

    tree = makeTree([2,1,3])
    assert printTree(invertTree(tree)) == [2,3,1]

    tree = makeTree([])
    assert printTree(invertTree(tree)) == []
    print("All tests passed!")

# Compare this BFS solution to BFS solution for
# LC 104: Maximum Depth of Binary Tree: https://github.com/rayning0/ctci/blob/master/neetcode/104_maximum_depth_of_binary_tree.py

# Why does LC 104 have

#         level_size = len(q)
#         for _ in range(level_size):

# But this solution does not?

# A rule you'll reuse:

# If the answer depends on levels
# Examples:
# - LC 102 Level Order Traversal
# - LC 104 Maximum Depth
# - LC 199 Right Side View
# - LC 637 Average of Levels
# ➡️ Process one level at a time.

# level_size = len(q)

# If the answer depends only on visiting every node
# Examples:
# - LC 226 Invert Tree
# - Tree search
# - Tree clone
# - Tree serialization
# ➡️ Just do

# while q:

# No for loop.
