# https://leetcode.com/problems/same-tree/description/
# https://neetcode.io/solutions/same-tree

from tree_helper import TreeNode, makeTree
from collections import deque

# 1. DFS
# Time: O(n), Space: O(h) <-- balanced tree O(log n), skewed tree O(n)
def isSameTree(p: TreeNode | None, q: TreeNode | None) -> bool:
    if not p or not q:
        return p is q
    # --- Means same as ---
    # if not p and not q:
    #     return True
    # if not p and q:
    #     return False
    # if p and not q:
    #     return False

    if p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

# 2. BFS
# Time: O(n), Space: O(n)
def isSameTree(p: TreeNode | None, q: TreeNode | None) -> bool:
    if not p or not q:
        return p is q

    queue = deque([(p, q)])
    while queue:
        n1, n2 = queue.popleft()

        # Both nodes missing? They're same, so move to next 2 nodes in queue.
        if not n1 and not n2:
            continue

        # Only 1 node missing. Not OK.
        if not n1 or not n2:
            return False
        # --- Means same as ---
        # if n1 and not n2:
        #     return False
        # if not n1 and n2:
        #     return False

        # Their values differ. Not OK.
        if n1.val != n2.val:
            return False

        # Compare children of both nodes
        queue.append((n1.left, n2.left))
        queue.append((n1.right, n2.right))

    return True

if __name__ == "__main__":
    p = makeTree([1,2,3])
    q = makeTree([1,2,3])
    assert isSameTree(p, q) == True

    p = makeTree([1,2])
    q = makeTree([1,None,2])
    assert isSameTree(p, q) == False

    p = makeTree([1,2,1])
    q = makeTree([1,1,2])
    assert isSameTree(p, q) == False
    print("All tests passed!")
