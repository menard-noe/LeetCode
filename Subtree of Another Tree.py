import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

            def sameTree(s: TreeNode, t: TreeNode) -> bool:
                if s is None and t is None:
                    return True
                elif s is None or t is None or s.val != t.val:
                    return False
                else:
                    return sameTree(s.left, t.left) and sameTree(s.right, t.right)

            if s is None or t is None:
                return False

            if sameTree(s, t):
                return True
            else:
                return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

if __name__ == "__main__":
    # execute only if run as a script
    tree = TreeNode(5)
    left = TreeNode(3)
    right = TreeNode(6)
    tree.right = right
    tree.left = left

    solution = Solution()
    print(solution.isSubtree(tree, tree))