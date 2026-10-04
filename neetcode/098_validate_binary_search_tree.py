# https://leetcode.com/problems/validate-binary-search-tree/description/
# https://neetcode.io/solutions/validate-binary-search-tree
# DFS: Preorder

# Instead of only comparing a node with its direct children,
# pass down a valid range (lower_bound, upper_bound) as you recurse.
# When you move to left child, update upper bound.
# When you move to right child, update lower bound.
# Initial upper/lower bounds = -infinity, +infinity

from tree_helper import TreeNode, makeTree

# Time: O(n), Space: O(h) <--- balanced tree O(log n), skewed tree O(n)
def isValidBST(root: TreeNode | None) -> bool:
    def dfs(node, lower, upper):
        if not node:
            return True

        if lower >= node.val or node.val >= upper:
            return False

        return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)

    return dfs(root, -float('inf'), float('inf'))

if __name__ == "__main__":
    assert isValidBST(makeTree([2,1,3])) == True
    assert isValidBST(makeTree([1,2,3])) == False
    assert isValidBST(makeTree([5,1,4,None,None,3,6])) == False
    assert isValidBST(makeTree([5,4,6,None,None,3,7])) == False
    print("All tests passed!")

#     5
#    / \
#   4   6
#      / \
#     3   7

# Your code sees 4 < 5, 6 > 5, 3 < 6, 7 > 6 — all pass. So it returns true.
# But node 3 is in right subtree of 5, and 3 < 5 — that violates the BST rule!
