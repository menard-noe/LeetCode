import math
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t2 is None:
            return t1
        elif t1 is None:
            return t2
        else:
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
            t1.val = t1.val + t2.val
            return t1



if __name__ == "__main__":
    # execute only if run as a script
    root = TreeNode(1)
    left = TreeNode(3)
    root.left = left
    right = TreeNode(2)
    root.right = right
    left_left = TreeNode(5)
    root.left.left = left_left

    root2 = TreeNode(2)
    left2 = TreeNode(1)
    right2 = TreeNode(3)
    left_right2 = TreeNode(4)
    right_right2 = TreeNode(7)
    root2.left = left2
    root2.right = right2
    root2.left.right = left_right2
    root2.right.right = right_right2


    solution = Solution()
    res = solution.mergeTrees(root, root2)
    print("")