# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = []

    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        def util(node: TreeNode, depth: int):
            if node.left is None and node.right is None:
                self.ans.append(depth)
                return

            if node.left:
                util(node.left, depth + 1)
            if node.right:
                util(node.right, depth + 1)

        util(root, 1)
        return min(self.ans)


if __name__ == "__main__":
    # execute only if run as a script
    tree = [1, 2, 3]
    solution = Solution()
    print(solution.minDepth(tree))
