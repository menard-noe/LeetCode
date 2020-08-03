import math
from typing import List
import sys


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices is None:
            return 0

        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

if __name__ == "__main__":
    # execute only if run as a script
    input = [7,1,5,3,6,4]
    solution = Solution()
    print(solution.maxProfit(input))