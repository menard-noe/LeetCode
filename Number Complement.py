import math
from typing import List


class Solution:
    def findComplement(self, num: int) -> int:
        mask_power = 0
        temp = num
        while temp != 0:
            temp = temp // 2
            mask_power += 1

        mask = pow(2, mask_power) - 1
        res = num ^ mask

        return res


if __name__ == "__main__":
    # execute only if run as a script
    nums = 5
    solution = Solution()
    print(solution.findComplement(nums))