import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        if root is None:
            return True

        def util(root: TreeNode) -> (int, bool):
            if not root:
                return 0, True

            height_left, valid_left = util(root.left)
            height_right, valid_right = util(root.right)

            valid = valid_left and valid_right and abs(height_left-height_right) < 2
            return 1 + max(height_left, height_right), valid

        _, valid = util(root)
        return valid


if __name__ == "__main__":
    # execute only if run as a script
    input = [3,9,20,None,None,15,7]
    solution = Solution()
    print(solution.isBalanced(input))