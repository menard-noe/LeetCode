# Definition for a binary tree node.
import math
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 0:
            return []

        result = [1]

        for row in range(1, rowIndex + 1):

            # Add 1 on the right, as next row is larger by 1.
            result.append(1)

            # Overwrite the middle elements in-place.
            prev = 1
            for i in range(1, row):
                new = result[i] + prev
                prev = result[i]
                result[i] = new

        return result


if __name__ == "__main__":
    # execute only if run as a script
    input = 5
    solution = Solution()
    print(solution.getRow(input))
