# Definition for a binary tree node.
import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        dico = dict()
        for i in range(0, int(math.floor(math.sqrt(c))) + 1):
            dico[i*i] = 1
        for key in dico:
            if c - key in dico:
                return True
        return False


if __name__ == "__main__":
    # execute only if run as a script
    input = 2
    solution = Solution()
    print(solution.judgeSquareSum(input))
