# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev_node = None
        current_node = head

        while current_node is not None:
            temp = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = temp

        return prev_node


if __name__ == "__main__":
    # execute only if run as a script
    Input = []
    solution = Solution()
    print(solution.reverseList(Input))