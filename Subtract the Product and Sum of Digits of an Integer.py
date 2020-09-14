from typing import List


class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        digits = []
        while n != 0:
            digits.append(n % 10)
            n = n // 10

        product = 1
        sum = 0

        for digit in digits:
            product *= digit
            sum += digit

        return product - sum



if __name__ == "__main__":
    # execute only if run as a script
    n = 4421
    solution = Solution()
    print(solution.subtractProductAndSum(n))