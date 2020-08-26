import math
from typing import List
import sys


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        prev = None
        while n != 0:
            rest = n % 2

            if prev is None:
                prev = rest
            else:
                if prev == rest:
                    return False
                prev = rest

            n = n // 2

        return True


if __name__ == "__main__":
    # execute only if run as a script
    input = 10
    solution = Solution()
    print(solution.hasAlternatingBits(input))