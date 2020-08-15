from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:

                    if i - 1 >= 0:
                        up = grid[i - 1][j]
                    else:
                        up = 0

                    if i + 1 < len(grid):
                        down = grid[i + 1][j]
                    else:
                        down = 0

                    if j - 1 >= 0:
                        left = grid[i][j - 1]
                    else:
                        left = 0

                    if j + 1 < len(grid[0]):
                        right = grid[i][j + 1]
                    else:
                        right = 0

                    res += (4 - up - down - left - right)
        return res


if __name__ == "__main__":
    # execute only if run as a script
    input = [[0, 1, 0, 0],
     [1, 1, 1, 0],
     [0, 1, 0, 0],
     [1, 1, 0, 0]]
    solution = Solution()
    print(solution.islandPerimeter(input))