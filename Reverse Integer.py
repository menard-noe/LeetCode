import math


class Solution:
    def reverse(self, x: int) -> int:
        negative_val = x < 0
        reversed_x = 0

        if negative_val:
            x *= -1

        while x > 0:
            reversed_x = reversed_x * 10 + x % 10  # can overflow !
            x = math.floor(x / 10)

        if negative_val:
            reversed_x *= -1

        if reversed_x > pow(2, 31) - 1 or reversed_x < - pow(2, 31):
            reversed_x = 0

        return reversed_x



if __name__ == "__main__":
    # execute only if run as a script
    Input = 1534236469
    solution = Solution()
    print(solution.reverse(Input))

