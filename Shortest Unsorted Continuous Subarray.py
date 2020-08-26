import math
from typing import List


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0

        minOutOfOrder = float('inf')
        maxOutOfOrder = float('-inf')
        for i in range(len(nums)):
            num = nums[i]
            if self.isOutOfOrder(i, num, nums):
                minOutOfOrder = min(num, minOutOfOrder)
                maxOutOfOrder = max(num, maxOutOfOrder)
        if minOutOfOrder == float('inf'):
            return 0
        subArrayLeftIdx = 0
        subArrayRightIdx = len(nums) - 1
        while minOutOfOrder >= nums[subArrayLeftIdx]:
            subArrayLeftIdx += 1
        while maxOutOfOrder <= nums[subArrayRightIdx]:
            subArrayRightIdx -= 1
        return (subArrayRightIdx - subArrayLeftIdx) + 1

    def isOutOfOrder(self, i, num, array):
        if i == 0:
            return num > array[i + 1]
        if i == len(array) - 1:
            return num < array[i - 1]
        return num > array[i + 1] or num < array[i - 1]


if __name__ == "__main__":
    # execute only if run as a script
    indices = [2, 6, 4, 8, 10, 9, 15]
    solution = Solution()
    print(solution.findUnsortedSubarray(indices))