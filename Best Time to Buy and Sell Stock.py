import math
from typing import List
import sys


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices is None:
            return 0
        cost_price = sys.maxsize
        profit = 0
        for price in prices:
            profit = max(profit, price - cost_price)
            cost_price = min(cost_price, price)
        return profit

if __name__ == "__main__":
    # execute only if run as a script
    input = [7,1,5,3,6,4]
    solution = Solution()
    print(solution.maxProfit(input))