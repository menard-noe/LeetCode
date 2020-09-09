from typing import List

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = -(heapq.heappop(stones))
            stone2 = -(heapq.heappop(stones))

            if stone1 == stone2:
                continue
            heapq.heappush(stones, -(abs(stone1 - stone2)))

        if len(stones) == 0:
            return 0
        else:
            return -(heapq.heappop(stones))


if __name__ == "__main__":
    # execute only if run as a script
    input = [2,7,4,1,8,1]
    solution = Solution()
    print(solution.lastStoneWeight(input))