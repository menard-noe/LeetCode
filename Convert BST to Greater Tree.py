import math
from typing import List

COUNT = [10]
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print2DUtil(root, space):
    # Base case
    if (root == None):
        return

    # Increase distance between levels
    space += COUNT[0]

    # Process right child first
    print2DUtil(root.right, space)

    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.val)

    # Process left child
    print2DUtil(root.left, space)


def print2D(root):
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)

class Solution:
    def __init__(self):
        self.total = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        if root is not None:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root


if __name__ == "__main__":
    # execute only if run as a script
    tree = TreeNode(2)
    left = TreeNode(0)
    right = TreeNode(3)
    left_left = TreeNode(-4)
    left_right = TreeNode(1)

    tree.right = right
    tree.left = left
    tree.left.left = left_left
    tree.left.right = left_right

    print2D(tree)
    print("------------------------------------------------------------------------------------------------")
    solution = Solution()
    solution.convertBST(tree)
    print2D(tree)
