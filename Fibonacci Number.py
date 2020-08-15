from typing import List


class Solution:
    def __init__(self):
        self.dico = dict()
        self.dico[0] = 0
        self.dico[1] = 1

    def fib(self, N: int) -> int:
        if N not in self.dico:
            self.dico[N] = self.fib(N - 1) + self.fib(N - 2)
        return self.dico[N]

if __name__ == "__main__":
    # execute only if run as a script
    input = 10
    solution = Solution()
    print(solution.fib(input))




