import math


# Definition for a binary tree node.
class Solution:
    def convertToBase7(self, num: int) -> str:
        res = ""
        negative = False

        if num == 0:
            return '0'

        if num < 0:
            num *= -1
            negative = True

        while num != 0:
            rest = num % 7
            num = num // 7
            res = str(rest) + res

        if negative:
            res = '-' + res
        return res


if __name__ == "__main__":
    # execute only if run as a script
    input = -7
    solution = Solution()
    print(solution.convertToBase7(input))
