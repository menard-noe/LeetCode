import math
from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:

        i = 0
        while True:
            if bits[i] == 1:
                i += 1
                if i >= len(bits) - 1:
                    return False
            i += 1
            if i >= len(bits) - 1:
                return True


if __name__ == "__main__":
    # execute only if run as a script
    bits = [1, 1, 1, 0]
    solution = Solution()
    print(solution.isOneBitCharacter(bits))