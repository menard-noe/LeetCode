# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return self.recu_depth(root)

    def recu_depth(self, root: TreeNode):
        if root is not None:
            return max(self.recu_depth(root.left) + 1, self.recu_depth(root.right) + 1)
        else:
            return 0

if __name__ == "__main__":
    # execute only if run as a script
    tree = [1, 2, 3]
    solution = Solution()
    print(solution.maxDepth(tree))
