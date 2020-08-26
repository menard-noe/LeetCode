
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if root is None:
            return 0
        list = []

        def utils(node: TreeNode):
            if node is not None:
                list.append(node.val)
                utils(node.left)
                utils(node.right)
        utils(root)

        list.sort()

        min = 999999999999
        for i in range(0, len(list) - 1):
            temp = list[i + 1] - list[i]
            if temp < min:
                min = temp
        return min


if __name__ == "__main__":
    tree = TreeNode(1)
    right = TreeNode(3)
    right_left = TreeNode(2)
    tree.right = right
    tree.right.left = right_left
    solution = Solution()
    print(solution.getMinimumDifference(tree))

