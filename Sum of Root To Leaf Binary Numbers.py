
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:

        def utils(node: TreeNode, binary: int) -> int:
            if node is None:
                return 0

            binary = binary * 2 + node.val
            if node.left is None and node.right is None:
                return binary
            else:
                return utils(node.left, binary) + utils(node.right, binary)

        if root is None:
            return 0

        return utils(root, 0)

if __name__ == "__main__":
    # execute only if run as a script
    tree = TreeNode(5)
    solution = Solution()
    print(solution.sumRootToLeaf(tree))