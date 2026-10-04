# https://leetcode.com/problems/search-in-a-binary-search-tree/description/
# https://algo.monster/liteproblems/700
# DFS: Search using main property of BST

# Use main property of Binary Search Tree:
# val < node.val  -> search left subtree
# val > node.val  -> search right subtree

from tree_helper import TreeNode, makeTree, printTree

# Time: O(h) <--- balanced O(log n), skewed O(n)
# Space: O(h) <--- balanced O(log n), skewed O(n)
def searchBST(root: TreeNode | None, val: int) -> TreeNode | None:
    def dfs(node):
        if not node or val == node.val:
            return node

        if val < node.val:
            return dfs(node.left)   # must RETURN result of dfs(). don't just traverse it.
        else:
            return dfs(node.right)

    return dfs(root)

# Inorder DFS passes, but NOT optimal! It ignores main property of a BST! Don't use.
# Time: O(n)
# Space: O(h)    <--- balanced O(log n), skewed O(n)
# def searchBST(root: TreeNode | None, val: int) -> TreeNode | None:
#     def dfs(node):
#         if not node:
#             return None

#         left = dfs(node.left)
#         if left is not None:
#             return left

#         if node.val == val:
#             return node

#         right = dfs(node.right)
#         if right is not None:
#             return right

#     return dfs(root)

if __name__ == "__main__":
    assert printTree(searchBST(makeTree([4,2,7,1,3]), 2)) == [2,1,3]
    assert printTree(searchBST(makeTree([4,2,7,1,3]), 5)) == []
    print("All tests passed!")
