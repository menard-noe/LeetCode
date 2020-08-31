# Definition for a binary tree node.
import math
from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        sum_tab = 0
        sum_n = 0
        dico = dict()
        double = - 1
        for i in range(0, len(nums)):
            if nums[i] in dico:
                double = nums[i]
            else:
                dico[nums[i]] = 1
            sum_tab += nums[i]
            sum_n += (i + 1)
        return [double, sum_n - (sum_tab - double)]

if __name__ == "__main__":
    # execute only if run as a script
    nums = [1, 2, 2, 4]
    solution = Solution()
    print(solution.findErrorNums(nums))