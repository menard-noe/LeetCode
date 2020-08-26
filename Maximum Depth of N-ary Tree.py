# Definition for a binary tree node.
import math

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0

        def util(node: Node) -> int:
            if not node:
                return 0
            if not node.children:
                return 1
            depth = max(util(child) for child in node.children) + 1
            return depth

        return util(root)


if __name__ == "__main__":
    # execute only if run as a script
    tree = Node(1)
    tree_a = Node(3)
    tree_b = Node(2)
    tree_c = Node(4)
    tree_a_a = Node(5)
    tree_a_b = Node(6)

    tree.children = [tree_a, tree_b, tree_c]
    tree_a.children = [tree_a_a, tree_a_b]

    solution = Solution()
    print(solution.maxDepth(tree))
