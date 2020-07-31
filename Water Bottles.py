from typing import List

import math


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        drinked_bottles = numBottles
        empty_bottles = numBottles

        while empty_bottles >= numExchange:
            temp_unused_empty_bottles = empty_bottles % numExchange
            exchanged_bottles = math.floor(empty_bottles / numExchange)

            drinked_bottles += exchanged_bottles
            empty_bottles = exchanged_bottles + temp_unused_empty_bottles

        return drinked_bottles


if __name__ == "__main__":
    # execute only if run as a script
    numBottles = 15
    numExchange = 4

    solution = Solution()
    print(solution.numWaterBottles(numBottles, numExchange))