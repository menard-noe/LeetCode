import math
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res += num
        size = len(nums)
        sum = ((size * size) + size) / 2
        return int(sum - res)


if __name__ == "__main__":
    # execute only if run as a script
    nums = [9,6,4,2,3,5,7,0,1]
    solution = Solution()
    print(solution.missingNumber(nums))