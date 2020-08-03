# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        elif q is None:
            return False
        elif p is None:
            return False
        elif p.val != q.val:
            return False

        return self.isSameTree(p.right, q.right) & self.isSameTree(p.left, q.left)

if __name__ == "__main__":
    # execute only if run as a script
    tree = [1, 2, 3]
    tree2 = [1, 2, 3]
    solution = Solution()
    print(solution.isSameTree(tree, tree2))
