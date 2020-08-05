import math
from typing import List


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0:
            if n & 1:
                res += 1
            n >>= 1
        return res

if __name__ == "__main__":
    # execute only if run as a script
    input = "00000000000000000000000000001011"
    solution = Solution()
    print(solution.hammingWeight(int(input,2)))