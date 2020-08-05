from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        first = None
        prev = None
        node = head

        while node is not None:
            if node.val == val:
                if prev is not None:
                    prev.next = node.next
                node = node.next
            else:
                if first is None:
                    first = node
                prev = node
                node = node.next
        return first



if __name__ == "__main__":
    # execute only if run as a script
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    solution = Solution()
    print(solution.removeElements(nums, val))




