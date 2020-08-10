from typing import List
import re


class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False
        if num == 1:
            return True
        while num != 2.0 and num != 3.0 and num != 5.0:
            a = num % 2
            b = num % 3
            c = num % 5

            if a == 0:
                num = num / 2
            elif b == 0:
                num = num / 3
            elif c == 0:
                num = num / 5
            else:
                return False

        return True


if __name__ == "__main__":
    # execute only if run as a script
    s = 7
    solution = Solution()
    print(solution.isUgly(s))