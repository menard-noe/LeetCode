import math
from typing import List


class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        sum = 0

        for val in A:
            if val % 2 == 0:
                sum += val

        res = []
        for query in queries:
            val = query[0]
            index = query[1]

            if A[index] % 2 == 0:
                sum -= A[index]

            A[index] += val

            if A[index] % 2 == 0:
                sum += A[index]

            res.append(sum)
        return res


if __name__ == "__main__":
    # execute only if run as a script
    A = [1, 2, 3, 4]
    queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
    solution = Solution()
    print(solution.sumEvenAfterQueries(A, queries))