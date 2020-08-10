# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.list = []
        self.utils(root, '')
        return self.list

    def utils(self, node: TreeNode, path: str):
        if node is not None:
            if node.left is None and node.right is None:
                self.list.append(path + str(node.val))
            path += str(node.val) + "->"
            self.utils(node.left, path)
            self.utils(node.right, path)
        else:
            return



if __name__ == "__main__":
    # execute only if run as a script
    input = [1,2,3]
    a = TreeNode(1)
    b = TreeNode(2)
    a.left = b
    c = TreeNode(3)
    a.right = c
    d = TreeNode(5)
    b.right = d
    solution = Solution()
    print(solution.binaryTreePaths(a))
