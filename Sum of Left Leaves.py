import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0

        def util(leaf: TreeNode, left: bool) -> int:
            if leaf is None:
                return 0
            elif leaf.left is None and leaf.right is None and left:
                return leaf.val
            else:
                return util(leaf.left, True) + util(leaf.right, False)

        return util(root, False)


if __name__ == "__main__":
    # execute only if run as a script
    input = TreeNode(5)
    left = TreeNode(3)
    right = TreeNode(8)
    input.left = left
    input.right = right
    right_left = TreeNode(7)
    right.left = right_left

    solution = Solution()
    print(solution.sumOfLeftLeaves(input))