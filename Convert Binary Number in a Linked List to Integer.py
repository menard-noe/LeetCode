# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        while head is not None:
            res = res * 2 + head.val
            head = head.next

        return res


if __name__ == "__main__":
    # execute only if run as a script
    head = ListNode(4)
    solution = Solution()
    print(solution.getDecimalValue(head))