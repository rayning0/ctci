# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
# https://neetcode.io/solutions/lowest-common-ancestor-of-a-binary-tree
# DFS: Preorder + MOSTLY Postorder

# Rules:
# “The lowest common ancestor of nodes p and q in tree is lowest node in the tree
# that has both p and q as descendants. We let a node be a descendant of itself.”
# - The number of nodes in tree is in range [2, 105].
# - All Node.val are unique.
# - p != q
# - p and q will exist in the tree.

from tree_helper import TreeNode, makeTree

# At any node, p or q can only be in 3 places:
# 1. Left subtree.
# 2. Right subtree.
# 3. Current node itself.

# dfs() doesn't return True/False. It returns the most useful node it found in that subtree.
# dfs() returns only 1 of 4 choices:
# None, p, q, or an already-found LCA.

# Time: O(n), Space: O(n)
def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def dfs(node):
        if not node:
            return None

        # Found 1 target. Return it upward.
        if node is p or node is q:
            return node

        left = dfs(node.left)
        right = dfs(node.right)

        # Found both targets. This node is the LCA!
        if (left is p and right is q) or (left is q and right is p):
        # if left and right:    <--- means same thing, but less intuitive
            return node

        return left or right
# Why use "left OR right" if we aren't returning boolean?
# If either left or right dfs() returns node (p or q) and the other dfs() returns None,
# we get "p or None = p" or "q or None = q". It returns a node, not boolean.

# Could it return "p or q = p", where both left AND right found nodes?
# NO, since line 38 already checked if we found both p and q.
# Only possible results of "left or right":

# left = p,    right = None
# left = q,    right = None
# left = None, right = p
# left = None, right = q
# left = None, right = None

    return dfs(root)

if __name__ == "__main__":
    # Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    # Output: 3
    # Explanation: The LCA of nodes 5 and 1 is 3.
    #
    #        3*
    #      /   \
    #     5*    1*
    #    / \   / \
    #   6  2  0  8
    #     / \
    #    7   4

    root = makeTree([3,5,1,6,2,0,8,None,None,7,4])
    assert lowestCommonAncestor(root, root.left, root.right) is root

    # Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    # Output: 5
    # Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
    #
    #        3
    #      /   \
    #     5*    1
    #    / \   / \
    #   6  2  0  8
    #     / \
    #    7   4*
    assert lowestCommonAncestor(root, root.left, root.left.right.right) is root.left

    root = makeTree([1,2])
    #   1
    #  /
    # 2
    assert lowestCommonAncestor(root, root, root.left) is root

    root = makeTree([3,5,None,6])
    #     3
    #    /
    #   5
    #  /
    # 6
    assert lowestCommonAncestor(root, root.left.left, root.left) is root.left

    root = makeTree([3,5,None,6,2,None,None,7,None])
    #     3
    #    /
    #   5
    #  / \
    # 6   2
    #    /
    #   7
    assert lowestCommonAncestor(root, root.left.right.left, root.left) is root.left
    print("All tests passed!")
