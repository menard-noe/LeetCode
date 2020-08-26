# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if root is None:
            return -1

        dico = dict()

        def utils(node: TreeNode) -> int:
            if node is None:
                return None

            left = utils(node.left)
            right = utils(node.right)

            if left is not None and right is not None:
                dico[min(utils(node.left), utils(node.right))] = 1
            else:
                dico[node.val] = 1
            return node.val

        utils(root)
        print(dico)
        if len(dico) >= 2:
            return sorted(set(dico))[1]
        else:
            return -1


if __name__ == "__main__":
    # execute only if run as a script
    nums = [1,3,5,6]
    target = 0
    solution = Solution()
    print(solution.findSecondMinimumValue(nums, target))