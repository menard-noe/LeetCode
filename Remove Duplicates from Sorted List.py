import math


#Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if not head:
            return None

        now = head
        while now.next:
            cur = now.next
            if cur.val == now.val:
                now.next = cur.next
            else:
                now = now.next
        return head




if __name__ == "__main__":
    # execute only if run as a script
    a = (1,2,3)
    b = "10"
    solution = Solution()
    print(solution.deleteDuplicates(a))