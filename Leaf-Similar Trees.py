# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        def utils(node: TreeNode, leaves: list):
            if node is None:
                return
            if node.right is None and node.left is None:
                leaves.append(node.val)
            else:
                utils(node.left, leaves)
                utils(node.right, leaves)

        list1 = []
        utils(root1, list1)

        list2 = []
        utils(root2, list2)

        return list1 == list2


if __name__ == "__main__":
    # execute only if run as a script
    root1 = TreeNode(4)
    root2 = TreeNode(6)
    solution = Solution()
    print(solution.leafSimilar(root1, root2))