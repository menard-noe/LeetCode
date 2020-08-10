from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root


if __name__ == "__main__":
    # execute only if run as a script
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(3)
    tree.right = TreeNode(7)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(9)


    solution = Solution()
    solution.invertTree(tree)
    print(tree)