# Definition for a binary tree node.
import math
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        max_val = -9999999
        max2 = -9999999
        max3 = -9999999

        min = 9999999
        min2 = 9999999

        for num in nums:

            if num > max_val:
                max3 = max2
                max2 = max_val
                max_val = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num

            if num < min:
                min2 = min
                min = num
            elif num < min2:
                min2 = num

        if min != 9999999 and min2 != 9999999:
            return max(max_val * max2 * max3, abs(min) * abs(min2) * max_val)
        return max_val * max2 * max3


if __name__ == "__main__":
    # execute only if run as a script
    input = [-4,-3,-2,-1,60]

    solution = Solution()
    print(solution.maximumProduct(input))
