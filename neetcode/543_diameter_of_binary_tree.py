# https://leetcode.com/problems/diameter-of-binary-tree/description/
# https://neetcode.io/solutions/diameter-of-binary-tree
# DFS

# Longest path through any node = height of its left subtree + height of its right subtree.

from tree_helper import TreeNode, makeTree

# DFS
# Time: O(n), Space: O(h) <-- balanced tree O(log n), skewed tree O(n)
def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    diam = 0

    # Almost same code as LC 104 (Maximum Depth of Binary Tree):
    # https://github.com/rayning0/ctci/blob/master/neetcode/104_maximum_depth_of_binary_tree.py
    def dfs(node):
        # "nonlocal" lets inner (nested) function change a variable defined in
        # its nearest enclosing function scope, so no need to make a new local variable.
        # This lets us change "diam" from outer function.
        nonlocal diam

        if not node:
            return 0

    # Longest path through any node = height of its left subtree + height of its right subtree.
        left = dfs(node.left)
        right = dfs(node.right)
        # diameter = longest path of all nodes for whole tree
        diam = max(diam, left + right)  # from tree heights, find diameter

        return 1 + max(left, right) # tree height

    dfs(root)
    return diam

# We see this same (inner dfs() function) pattern in many tree problems:
# - LC 543 Diameter of Binary Tree
# - LC 124 Binary Tree Maximum Path Sum
# - LC 110 Balanced Binary Tree (depending on implementation)
# - many recursive tree DP problems

# It's a canonical recursion pattern worth learning. It gives the helper access to shared state (answer) while keeping that state local to the main function.

if __name__ == "__main__":
    assert diameterOfBinaryTree(makeTree([1,2,3,4,5])) == 3
    assert diameterOfBinaryTree(makeTree([1,2])) == 1
    assert diameterOfBinaryTree(makeTree([1,None,2,3,4,5])) == 3
    assert diameterOfBinaryTree(makeTree([1,2,3])) == 2
    print("All tests passed!")

# Q: Why does this question NOT have a BFS solution?

# BFS visits nodes in the wrong order, left to right horizontally. It doesn't know each node's height.
# BFS is good when answer depends on distance from root, from top down.
# But diameter depends on distance BELOW each node, a bottom-up question.

# Use BFS when answer depends on levels:
# 102 Level Order
# 104 Maximum Depth
# 199 Right Side View

# Use DFS when a parent depends on info from its children:
# 104 Maximum Depth (recursive)
# 543 Diameter
# 110 Balanced Tree
# 124 Maximum Path Sum
