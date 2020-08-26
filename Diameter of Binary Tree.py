from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0

        def utils(node: TreeNode, ans: [int]) -> int:
            if node is None:
                return 0

            left = utils(node.left, ans)
            right = utils(node.right, ans)

            ans[0] = max(ans[0], left + right)
            return max(left, right) + 1

        ans = [0]
        utils(root, ans)
        return ans[0]


if __name__ == "__main__":
    # execute only if run as a script
    tree = TreeNode(5)
    left = TreeNode(3)
    right = TreeNode(6)
    tree.right = right
    tree.left = left

    solution = Solution()
    print(solution.diameterOfBinaryTree(tree))




