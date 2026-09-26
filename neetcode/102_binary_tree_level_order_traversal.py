# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# https://neetcode.io/solutions/binary-tree-level-order-traversal
# BFS

from tree_helper import TreeNode, makeTree
from collections import deque

# BFS
# Time: O(n), Space: O(n)
def levelOrder(root: TreeNode | None) -> list[list[int]]:
    if not root:
        return []

    q = deque([root])
    ans = []

    while q:
        level_size = len(q)
        level = []

        for _ in range(level_size):
            node = q.popleft()
            level.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        ans.append(level)

    return ans

if __name__ == "__main__":
    assert levelOrder(makeTree([3,9,20,None,None,15,7])) == [[3],[9,20],[15,7]]
    assert levelOrder(makeTree([1,2,3,4,5,6,7])) == [[1],[2,3],[4,5,6,7]]
    assert levelOrder(makeTree([1])) == [[1]]
    assert levelOrder(makeTree([])) == []
    print("All tests passed!")

# *** Good BFS template: ***

# q = deque([root])

# while q:
#     level_size = len(q)

#     for _ in range(level_size):
#         node = q.popleft()

#         # process node

#         if node.left:
#             q.append(node.left)
#         if node.right:
#             q.append(node.right)

#     # process entire level

# Then, depending on the problem:
# LC 102 → level.append(node.val) and ans.append(level)
# LC 104 → depth += 1
# LC 199 (Right Side View) → save the last node's value for each level
# LC 637 (Average of Levels) → compute the average of level
