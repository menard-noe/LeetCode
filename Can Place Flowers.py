import math
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.insert(0, 0)
        flowerbed.append(0)

        if len(flowerbed) == 0:
            return False
        i = 1
        while n != 0:
            if i >= len(flowerbed) - 1:
                return False

            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
                i += 1
            i += 1
        return True


if __name__ == "__main__":
    # execute only if run as a script
    input = [1,0,0,0,1,0,0]
    n = 3
    solution = Solution()
    print(solution.canPlaceFlowers(input, n))