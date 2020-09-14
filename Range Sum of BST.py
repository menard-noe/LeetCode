# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root is None:
            return 0

        if L <= root.val <= R:
            return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
        else:
            return self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)



if __name__ == "__main__":
    # execute only if run as a script
    root = TreeNode(5)
    L = 7
    R = 15
    solution = Solution()
    print(solution.rangeSumBST(root, L, R))


