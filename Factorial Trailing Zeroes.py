from typing import List


class Solution:
    def trailingZeroes(self, n: int) -> int:
        counter = 0

        while n >= 5:
            counter += n // 5
            n = n // 5

        return counter



if __name__ == "__main__":
    # execute only if run as a script
    input = 30
    solution = Solution()
    print(solution.trailingZeroes(input))




