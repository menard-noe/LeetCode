import math
from typing import List


class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'

        map = '0123456789abcdef'

        res = ""
        if num < 0:
            num += 2 ** 32

        while num > 0:
            rest = num % 16
            num = (num) // 16

            res += str(map[rest])

        return res[::-1]


if __name__ == "__main__":
    # execute only if run as a script
    input = 256
    solution = Solution()
    print(solution.toHex(input))