import math


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        dico = dict()
        dico2 = dict()
        if root is None:
            return []

        def utils(node: TreeNode, depth: int) -> None:
            if node is None:
                return
            else:
                dico[depth] = dico.get(depth, 0) + node.val
                dico2[depth] = dico2.get(depth, 0) + 1

                utils(node.left, depth + 1)
                utils(node.right, depth + 1)
        utils(root, 0)

        res = []
        for key in dico:
            res.append(dico[key] / dico2[key])
        return res


if __name__ == "__main__":
    # execute only if run as a script
    a = TreeNode(1)
    b = TreeNode(2)
    a.left = b
    c = TreeNode(3)
    a.right = c
    d = TreeNode(5)
    b.right = d

    solution = Solution()
    print(solution.averageOfLevels(a))