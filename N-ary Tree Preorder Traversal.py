import math
from typing import List


# Definition for a Node.
class Node:
  def __init__(self, val=None, children=None):
      self.val = val
      self.children = children



class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        if root is None:
            return res

        def util(node: 'Node')-> None:
            if Node is None:
                return
            else:
                res.append(node.val)
                if node.children is not None:
                    for child in node.children:
                        util(child)
        util(root)
        return res


if __name__ == "__main__":
    # execute only if run as a script
    node = Node(5)
    solution = Solution()
    print(solution.preorder(node))