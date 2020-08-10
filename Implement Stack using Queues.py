from typing import List


class MyStack:

    def __init__(self):
        self.a = []

    def push(self, x: int) -> None:
        self.a.append(x)

    def pop(self) -> int:
        temp = []

        for i in range(len(self.a) - 1, -1, -1):
            temp.append(self.a[i])
        x = temp[0]
        self.a = self.a[:-1]
        return x

    def top(self) -> int:
        temp = []
        for i in range(len(self.a)-1, -1, -1):
            temp.append(self.a[i])
        x = temp[0]
        return x

    def empty(self) -> bool:
        return len(self.a) == 0


if __name__ == "__main__":
    # execute only if run as a script
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    print(stack.top())  # returns 2
    print(stack.pop())  # returns 2
    print(stack.empty())  # returns false
    print(stack)
