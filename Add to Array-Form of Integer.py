import math
from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A_integer = 0
        index = 1

        for i in reversed(A):
            A_integer += i * index
            index *= 10

        res = A_integer + K

        res_array = []
        if res == 0:
            res_array.append(0)
            return res_array

        while res != 0:
            mod = res % 10
            res_array.append(mod)
            res //= 10
        res_array.reverse()
        return res_array


if __name__ == "__main__":
    A = [1, 2, 0, 0]
    K = 34
    solution = Solution()
    print(solution.addToArrayForm(A, K))