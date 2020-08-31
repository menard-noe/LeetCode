# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if root.val == val:
            return root
        else:
            return self.searchBST(root.left, val) or self.searchBST(root.right, val)




if __name__ == "__main__":
    # execute only if run as a script
    tree = TreeNode(5)
    tree2 = TreeNode(2)
    tree3 = TreeNode(4)
    tree.left = tree2
    tree.right = tree3
    val = 2
    solution = Solution()
    x = solution.searchBST(tree, val)
    print(x)
