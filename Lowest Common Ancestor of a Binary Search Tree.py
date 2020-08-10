from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        current_node_val = root.val

        p_val = p.val
        q_val = q.val

        if p_val > current_node_val and q_val > current_node_val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p_val < current_node_val and q_val < current_node_val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root



if __name__ == "__main__":
    # execute only if run as a script
    Input = ["flower","flow","flight"]
    solution = Solution()
    print(solution.longestCommonPrefix(Input))
