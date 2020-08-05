# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        A_pointer = headA
        B_pointer = headB

        while A_pointer != B_pointer:
            if A_pointer is None:
                A_pointer = headB
            else:
                A_pointer = A_pointer.next

            if B_pointer is None:
                B_pointer = headA
            else:
                B_pointer = B_pointer.next

        return A_pointer


if __name__ == "__main__":
    # execute only if run as a script
    solution = Solution()
