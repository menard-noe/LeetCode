from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        for column in grid:
            for val in column:
                if val < 0:
                    res += 1

        return res


if __name__ == "__main__":
    grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    solution = Solution()
    print(solution.countNegatives(grid))