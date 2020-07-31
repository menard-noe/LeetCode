import math


class Solution:
    def addDigits(self, num: int) -> int:

        while num > 9:
            num = self.add_digits_might_be_superior_9(num)
        return num

    def add_digits_might_be_superior_9(self, num: int):
        res = 0
        while num > 9:
            res += num % 10
            num = math.floor(num / 10)
        res += num
        return res

if __name__ == "__main__":
    # execute only if run as a script
    input = 38
    solution = Solution()
    print(solution.addDigits(input))