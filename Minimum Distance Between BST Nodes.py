
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        res = []

        def utils(node: TreeNode):
            if node is None:
                return
            else:
                res.append(node.val)
                utils(node.left)
                utils(node.right)
        utils(root)
        res.sort()
        return min(res[i + 1] - res[i] for i in range(0, len(res) - 1))



if __name__ == "__main__":
    # execute only if run as a script
    root = TreeNode(5)
    solution = Solution()
    print(solution.minDiffInBST(root))
