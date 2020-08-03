# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """list = []
        node = head
        while node is not None:
            if node in list:
                return True
            else:
                list.append(node)
                node = node.next
        return False"""
        if head is None or head.next is None:
            return False

        slow = head
        fast = head.next

        while slow is not fast:
            if fast is None or fast.next is None:
                return False
            else:
                slow = slow.next
                fast = fast.next.next
        return True

if __name__ == "__main__":
    # execute only if run as a script
    tree = [1, 2, 3]
    solution = Solution()
    print(solution.hasCycle(tree))
