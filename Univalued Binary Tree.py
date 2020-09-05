
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:

        def utils(node: TreeNode, val: int):
            if node is None:
                return True
            elif node.val == val:
                return utils(node.left, val) and utils(node.right, val)
            else:
                return False

        if root is None:
            return False
        return utils(root, root.val)


if __name__ == "__main__":
    # execute only if run as a script
    tree = TreeNode(5)
    solution = Solution()
    print(solution.isUnivalTree(tree))