from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node: ListNode):
        node.val, node.next = node.next.val, node.next.next
        return



if __name__ == "__main__":
    # execute only if run as a script
    input = [4, 5, 9]
    solution = Solution()
    print(solution.deleteNode(input))




