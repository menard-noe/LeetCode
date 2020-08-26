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
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def utils(node: TreeNode):
            if node:
                utils(node.left)
                node.left = None
                self.res.right = node
                self.res = self.res.right
                utils(node.right)

        self.res = TreeNode(None)
        self.res_root = self.res
        utils(root)
        return self.res_root.right


if __name__ == "__main__":
    # execute only if run as a script
    tree = TreeNode(5)
    left = TreeNode(3)
    right = TreeNode(6)
    left_left = TreeNode(2)
    left_right = TreeNode(4)
    left_left_left = TreeNode(1)
    right_right = TreeNode(8)
    right_right_left = TreeNode(7)
    right_right_right = TreeNode(9)

    tree.right = right
    tree.left = left
    tree.left.left = left_left
    tree.left.right = left_right
    tree.left.left.left = left_left_left
    tree.right.right = right_right
    tree.right.right.left = right_right_left
    tree.right.right.right = right_right_right

    print2D(tree)
    print("------------------------------------------------------------------------------------------------")
    solution = Solution()
    print2D(solution.increasingBST(tree))
