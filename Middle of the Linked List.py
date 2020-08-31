from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        node_fast = head
        node_slow = head

        while node_fast is not None:
            node_fast = node_fast.next
            if node_fast is not None:
                node_fast = node_fast.next
                node_slow = node_slow.next
        return node_slow


if __name__ == "__main__":
    # execute only if run as a script
    input = ListNode()
    solution = Solution()
    print(solution.middleNode(input))
