# Definition for a binary tree node.
import math
from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []

        def self_dividing(i: int):
            temp_i = i
            while i != 0:
                rest = i % 10
                if rest == 0:
                    return False
                if temp_i % rest != 0:
                    return False
                i = i // 10
            return True

        for i in range(left, right + 1):
            if self_dividing(i):
                res.append(i)

        return res

if __name__ == "__main__":
    # execute only if run as a script
    left = 1
    right = 22
    target = 0
    solution = Solution()
    print(solution.selfDividingNumbers(left, right))