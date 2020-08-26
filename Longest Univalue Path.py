from typing import List
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longestUnivaluePath(self, root):
        def dfs(node, prev_val):
            if node is None:
                return 0
            left = dfs(node.left, node.val)
            right = dfs(node.right, node.val)
            self.max_val = max(self.max_val, left + right)
            if node.val == prev_val:
                return max(left, right) + 1
            return 0

        self.max_val = 0
        if root is None:
            return 0
        dfs(root, root.val)
        return self.max_val


if __name__ == "__main__":
    # execute only if run as a script

    root = TreeNode(5)

    solution = Solution()
    print(solution.longestUnivaluePath(root))
