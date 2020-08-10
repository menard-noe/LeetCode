# Definition for singly-linked list.
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        if not head:
            return True

        self.head = head
        self.flag = 0

        mover = head

        def recurTail(mover: ListNode):
            if mover:
                recurTail(mover.next)

                if mover.val != self.head.val:
                    self.flag = 1
                self.head = self.head.next

        recurTail(mover)
        return False if self.flag else True


if __name__ == "__main__":
    # execute only if run as a script
    input = [1,2]
    solution = Solution()
    print(solution.isPalindrome(input))