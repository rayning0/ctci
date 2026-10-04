# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# https://neetcode.io/solutions/kth-smallest-element-in-a-bst
# DFS: Inorder

# Use inorder DFS if you must traverse nodes in SORTED ORDER

# A binary search tree (BST) satisfies the following constraints:
# Left subtree of every node contains only nodes with keys < the node's key.
# Right subtree of every node contains only nodes with keys > the node's key.
# Both left and right subtrees are also binary search trees.

from tree_helper import TreeNode, makeTree

# Solution 1 stores answer in nonlocal variable, so dfs() doesn't return it.
# Solution 2 returns answer through recursive calls, so each caller must immediately return it upward.

# 1. Easier to remember, but it visits ALL nodes, even after target found.
# We only need dfs() to traverse nodes, NOT to return or store the answer.
# Instead, we store answer in shared variable ans.

# Time: O(n)
# Space: O(h) <--- balanced O(log n), skewed O(n)
def kthSmallest(root: TreeNode | None, k: int) -> int:
    count = 0
    ans = 0

    def dfs(node):
        nonlocal count, ans

        if not node:
            return

        dfs(node.left)

        count += 1
        if count == k:
            ans = node.val
            return ans

        dfs(node.right)

    dfs(root)
    return ans

# 2. Optimal: Exits early if target found.
# dfs() both does traversal AND returns answer.
# Each caller must immediately propagate that answer upward.

# Time: O(k + h), worse case O(n)
# Space: O(h)    <--- balanced O(log n), skewed O(n)
def kthSmallest(root: TreeNode | None, k: int) -> int:
    count = 0

    def dfs(node):
        nonlocal count

        if not node:
            return

        left = dfs(node.left)
# If left subtree already found answer, return it immediately.
# Unlike Solution 1, this propagates answer upward so recursion stops early.
        if left:
            return left

        count += 1
        if count == k:
            return node.val

        right = dfs(node.right)
# Unlike Solution 1, this propagates answer upward so recursion stops early.
        if right:
            return right

    return dfs(root)

if __name__ == "__main__":
    assert kthSmallest(makeTree([3,1,4,None,2]), 1) == 1
    assert kthSmallest(makeTree([2,1,3]), 1) == 1
    assert kthSmallest(makeTree([5,3,6,2,4,None,None,1]), 4) == 4
    assert kthSmallest(makeTree([4,3,5,2,None]), 4) == 5
    print("All tests passed!")
