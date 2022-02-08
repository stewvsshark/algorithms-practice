# There is a binary tree with N nodes.
# You are viewing the tree from its left side and can see only the leftmost nodes at each level.
# Return the number of visible nodes.
# Note: You can see only the leftmost nodes,
#   but that doesn't mean they have to be left nodes. The leftmost node at a level could be a right node.

# Insight: there must be at least 1 left most node at every level of the tree

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def visible_nodes(root):
    if root.left is None and root.right is None:
        return 1
    else:
        if root.left is not None and root.right is None:
            return 1 + visible_nodes(root.left)
        elif root.right is not None and root.left is None:
            return 1 + visible_nodes(root.right)
        else:
            return 1 + max(visible_nodes(root.left), visible_nodes(root.right))


root_1 = TreeNode(8)
root_1.left = TreeNode(3)
root_1.right = TreeNode(10)
root_1.left.left = TreeNode(1)
root_1.left.right = TreeNode(6)
root_1.left.right.left = TreeNode(4)
root_1.left.right.right = TreeNode(7)
root_1.right.right = TreeNode(14)
root_1.right.right.left = TreeNode(13)

print(visible_nodes(root_1))  # 4

root_2 = TreeNode(10)
root_2.left = TreeNode(8)
root_2.right = TreeNode(15)
root_2.left.left = TreeNode(4)
root_2.left.left.right = TreeNode(5)
root_2.left.left.right.right = TreeNode(6)
root_2.right.left = TreeNode(14)
root_2.right.right = TreeNode(16)

print(visible_nodes(root_2))  # 5
