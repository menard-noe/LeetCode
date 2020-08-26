import math
from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        i_length = len(nums)
        j_length = len(nums[0])

        newMatrix = []

        if i_length * j_length != r * c:
            return nums
        c_index = 0

        temp = []
        for i in range(0, i_length):
            for j in range(0, j_length):
                temp.append(nums[i][j])
                c_index += 1
                if c_index >= c:
                    c_index = 0
                    newMatrix.append(temp)
                    temp = []


        return newMatrix


if __name__ == "__main__":
    # execute only if run as a script
    nums =[[1, 2],[3, 4]]
    r = 2
    c = 4
    solution = Solution()
    print(solution.matrixReshape(nums, r, c))

