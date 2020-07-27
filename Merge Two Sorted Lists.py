# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.head = self.ref = None

    def append(self, node):
        if not self.head:
            self.head = self.ref = node
        else:
            self.ref.next = node
            self.ref = self.ref.next

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        while l1 and l2:
            if l1.val < l2.val:
                next = l1
                l1 = l1.next
            else:
                next = l2
                l2 = l2.next

            self.append(next)

        if l1:
            self.append(l1)
        elif l2:
            self.append(l2)
        return self.head


