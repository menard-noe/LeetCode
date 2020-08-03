# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.compare(root.left, root.right)

    def compare(self, left_node: TreeNode, right_node: TreeNode):
        if left_node is None and right_node is None:
            return True
        elif left_node is None or right_node is None:
            return False
        return left_node.val == right_node.val \
               and self.compare(left_node.left, right_node.right) \
               and self.compare(left_node.right, right_node.left)


if __name__ == "__main__":
    # execute only if run as a script
    tree = [1, 2, 3]
    solution = Solution()
    print(solution.isSymmetric(tree))
