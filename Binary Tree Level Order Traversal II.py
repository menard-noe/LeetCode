import math


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        dico = dict()
        list = []

        if root is None:
            return []

        self.helper(root, dico, 0)

        for key in dico.keys():
            list.append(dico[key])
        list.reverse()
        return list

    def helper(self, node: TreeNode, dico: dict, depth):
        if node is None:
            return
        else:
            if depth in dico:
                same_level_val = dico[depth]
                same_level_val.append(node.val)
                dico[depth] = same_level_val
            else:
                dico[depth] = [node.val]
            self.helper(node.left, dico, depth + 1)
            self.helper(node.right, dico, depth + 1)
        return

if __name__ == "__main__":
    # execute only if run as a script
    input = [3,9,20,None,None,15,7]

    a = TreeNode(15)
    b = TreeNode(7)
    c = TreeNode(20, a, b)
    d = TreeNode(9)
    e = TreeNode(3, d, c)

    solution = Solution()
    print(solution.levelOrderBottom(e))