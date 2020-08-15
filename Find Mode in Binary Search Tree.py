import collections
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        def get_value(values_dict, root):
            if root is not None:
                value = root.val
                if value not in values_dict:
                    values_dict[value] = 1
                else:
                    values_dict[value] += 1
                values_dict = get_value(values_dict, root.left)
                values_dict = get_value(values_dict, root.right)
            return values_dict

        values_dict = get_value(dict(), root)
        max_frequence = max(values_dict.values())
        return [node for node, count in values_dict.items() if count == max_frequence]

if __name__ == "__main__":
    # execute only if run as a script
    tree = TreeNode(1)
    right = TreeNode(2)
    right_left = TreeNode(2)
    tree.right = right
    tree.right.left = right_left

    solution = Solution()
    print(solution.findMode(tree))
