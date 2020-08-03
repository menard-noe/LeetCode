# Definition for a binary tree node.
import math
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        list = [[1]]
        for i in range(1, numRows):
            row = [None for _ in range(i + 1)]
            row[0] = 1
            row[-1] = 1

            for j in range(1, i):
                row[j] = (list[i - 1][j] + list[i - 1][j - 1])
            list.append(row)
        return list


if __name__ == "__main__":
    # execute only if run as a script
    input = 5
    solution = Solution()
    print(solution.generate(input))
