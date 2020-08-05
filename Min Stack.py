# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math


class LinkedList:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.min = math.inf


class MinStack:
    def __init__(self):
        self.head = None

    def push(self, x: int) -> None:
        node = LinkedList(x)

        if self.head is None:
            node.min = node.val
        else:
            node.min = min(node.val, self.head.min)
            node.prev = self.head

        self.head = node

    def pop(self) -> None:
        if self.head is not None:
            self.head = self.head.prev

    def top(self) -> int:
        if self.head is not None:
            return self.head.val

    def getMin(self) -> int:
        if self.head is not None:
            return self.head.min

if __name__ == "__main__":
    # execute only if run as a script
    stack = MinStack()
    stack.push(5)
    stack.push(10)
    stack.push(-5)
    stack.push(3)
    stack.push(7)
    stack.push(0)
    stack.push(-12)
    print(stack)
