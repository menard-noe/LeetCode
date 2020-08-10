import math
from typing import List


class Solution:
    def canWinNim(self, n: int) -> bool:
            if n % 4 == 0:
                return False
            else:
                return True

if __name__ == "__main__":
    # execute only if run as a script
    nums = 4
    solution = Solution()
    print(solution.canWinNim(nums))