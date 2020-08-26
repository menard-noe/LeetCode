import math
from typing import List


# Definition for a Node.
class Node:
  def __init__(self, val=None, children=None):
      self.val = val
      self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        """
        res = []
        if root is None:
            return res

        def util(node: 'Node')-> None:
            if Node is None:
                return
            else:
                if node.children is not None:
                    for child in node.children:
                        util(child)
                res.append(node.val)
        util(root)
        return res
        """
        if not root: return []
        stack = [root]
        out = []
        while len(stack):
            top = stack.pop()
            out.append(top.val)
            stack.extend(top.children)
        return out[::-1]

if __name__ == "__main__":
    # execute only if run as a script
    node_a = Node(5, [])
    node_e = Node(6, [])
    node_b = Node(3, [node_a, node_e])
    node_c = Node(2, [])
    node_d = Node(4, [])
    root = Node(1, [node_b, node_c, node_d])

    solution = Solution()
    print(solution.postorder(root))