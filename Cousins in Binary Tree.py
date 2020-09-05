
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.x_parent = [None, None]
        self.y_parent = [None, None]

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        def utils(node: TreeNode, parent: TreeNode, x: int, y: int, depth: int):
            if node is None:
                return

            if node.val == x:
                self.x_parent = [parent, depth]
            elif node.val == y:
                self.y_parent = [parent, depth]

            utils(node.left, node, x, y, depth + 1)
            utils(node.right, node, x, y, depth + 1)
            return

        utils(root, None, x, y, 0)
        if self.x_parent[0] != self.y_parent[0] and self.x_parent[1] == self.y_parent[1]:
            return True
        else:
            return False


if __name__ == "__main__":
    # execute only if run as a script
    tree = TreeNode(5)
    x = 4
    y = 3
    solution = Solution()
    print(solution.isCousins(tree, x, y))




