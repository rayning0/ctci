# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
# https://neetcode.io/solutions/lowest-common-ancestor-of-a-binary-search-tree
# Iterative / DFS

# Rules:
# “The lowest common ancestor of nodes p and q in tree is lowest node in the tree
# that has both p and q as descendants. We let a node be a descendant of itself.”
# - The number of nodes in tree is in range [2, 10^5].
# - All Node.val are unique.
# - p != q
# - p and q will exist in the tree.

from tree_helper import TreeNode, makeTree

# BST property:
# - If both targets are left, search left.
# - If both targets are right, search right.
# - Otherwise, current node is the LCA.

# 1. DFS
# Time: O(h) <--- balanced O(log n), skewed O(n)
# Space: O(h) <--- balanced O(log n), skewed O(n)
def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def dfs(node):
        if not node:
            return None

        # Both targets in left subtree
        if p.val < node.val and q.val < node.val:
            return dfs(node.left)   # must RETURN result of dfs(). don't just traverse it.

        # Both targets in right subtree
        if p.val > node.val and q.val > node.val:
            return dfs(node.right)

        # Found LCA!
        return node
        # If we hit this line, 1 of 4 cases is true:
            # 1. p < node < q
            # 2. q < node < p
            # 3. node == p
            # 4. node == q

    return dfs(root)

# 2. Iterative. BETTER!
# Time: O(h) <--- balanced O(log n), skewed O(n)
# Space: O(1)
def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    curr = root

    while curr:
        if p.val < curr.val and q.val < curr.val:
            curr = curr.left
        elif p.val > curr.val and q.val > curr.val:
            curr = curr.right
        else:
            return curr

# See https://github.com/rayning0/ctci/blob/master/neetcode/236_lowest_common_ancestor_of_a_binary_tree.py
# This solution passes, but NOT optimal! Don't use. It doesn't use BST property!

# Time: O(n), Space: O(n)
# def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#     def dfs(node):
#         if not node:
#             return None

#         # Found 1 target. Return it upward.
#         if node is p or node is q:
#             return node

#         left = dfs(node.left)
#         right = dfs(node.right)

#         # Found both targets. This node is the LCA!
#         # if (left is p and right is q) or (left is q and right is p):
#         if left and right:
#             return node

#         return left or right

#     return dfs(root)

if __name__ == "__main__":
    root = makeTree([6,2,8,0,4,7,9,None,None,3,5])
    assert lowestCommonAncestor(root, root.left, root.right) is root
    assert lowestCommonAncestor(root, root.left, root.left.right) is root.left

    root = makeTree([2,1])
    assert lowestCommonAncestor(root, root, root.left) is root

    root = makeTree([5,3,8,1,4,7,9,None,2])
    assert lowestCommonAncestor(root, root.left.right, root.left) is root.left
    print("All tests passed!")
