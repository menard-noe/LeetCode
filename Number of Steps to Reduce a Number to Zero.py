import heapq
from typing import List


class Solution:
    def numberOfSteps(self, num: int) -> int:
        res = 0
        while num != 0:
            if num % 2 == 0:
                num = num / 2
            else:
                num = num - 1
            res += 1

        return res


if __name__ == "__main__":
    # execute only if run as a script
    num = 0
    solution = Solution()
    print(solution.numberOfSteps(num))
