import math
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, t: TreeNode) -> str:

        if t is None:
            return ""

        def utils(node: TreeNode, left: bool, nodeTemp: TreeNode) -> str:
            if node is not None:
                return "(" + str(node.val) + utils(node.left, True, node.right) + utils(node.right, False, None) + ")"
            elif left and nodeTemp is not None:
                return "()"
            else:
                return ""


        res = utils(t, False, None)
        return res[1:-1]


if __name__ == "__main__":
    # execute only if run as a script
    input = [1,2,3,3]
    a = TreeNode(1)
    b = TreeNode(2)
    a.left = b
    c = TreeNode(3)
    a.right = c
    d = TreeNode(5)
    b.right = d

    solution = Solution()
    print(solution.tree2str(a))