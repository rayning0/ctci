class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

# Example from LC 104: root = [3,9,20,None,None,15,7]
def makeTree(vals: list[int | None]) -> TreeNode | None:
    """Create a binary tree from a level-order array."""
    if not vals or vals[0] is None:
        return None

    root = TreeNode(vals[0])
    nodes = deque([root])
    values = iter(vals[1:])

    while nodes:
        node = nodes.popleft()

        left_val = next(values, None)
        if left_val is not None:
            node.left = TreeNode(left_val)
            nodes.append(node.left)

        right_val = next(values, None)
        if right_val is not None:
            node.right = TreeNode(right_val)
            nodes.append(node.right)

    return root

# same function without iter() or next():

    # if not vals or vals[0] is None:
    #     return None

    # root = TreeNode(vals[0])
    # nodes = deque([root])
    # i = 1

    # while nodes and i < len(vals):
    #     node = nodes.popleft()

    #     left_val = vals[i]
    #     if left_val is not None:
    #         node.left = TreeNode(left_val)
    #         nodes.append(node.left)
    #     i += 1

    #     right_val = vals[i]
    #     if i < len(vals) and right_val is not None:
    #         node.right = TreeNode(right_val)
    #         nodes.append(node.right)
    #     i += 1
    # return root

def printTree(root: TreeNode | None) -> None:
    """Print a binary tree as a trimmed level-order list."""
    if root is None:
        print([])
        return

    values = []
    nodes = deque([root])

    while nodes:
        node = nodes.popleft()
        if node is None:
            values.append(None)
            continue

        values.append(node.val)
        nodes.append(node.left)
        nodes.append(node.right)

    while values and values[-1] is None:
        values.pop()

    print(values)
