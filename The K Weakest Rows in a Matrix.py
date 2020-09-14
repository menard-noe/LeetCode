import heapq
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        heap = []
        heapq.heapify(heap)
        for row in range(len(mat)):
            soldiers = 0
            for j in mat[row]:
                if j == 1:
                    soldiers += 1
            heapq.heappush(heap, (soldiers, row))

        res = []
        for i in range(k):
            res.append((heapq.heappop(heap))[1])

        return res


if __name__ == "__main__":
    # execute only if run as a script
    mat = [[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]]
    k = 2
    solution = Solution()
    print(solution.kWeakestRows(mat, k))
