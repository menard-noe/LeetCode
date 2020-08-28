# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if root is None:
            return False

        dico = dict()

        def utils(node: TreeNode, k: int, dico: dict()) -> bool:
            if node is None:
                return False
            elif k - node.val in dico:
                return True
            else:
                dico[node.val] = 1
                return utils(node.left, k, dico) or utils(node.right, k, dico)

        return utils(root, k, dico)

if __name__ == "__main__":
    # execute only if run as a script
    tree = TreeNode(5)
    target = 9
    solution = Solution()
    print(solution.findTarget(tree, target))