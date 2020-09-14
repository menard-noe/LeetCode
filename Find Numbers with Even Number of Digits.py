from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        def get_number_digit(number) -> int:
            number_digit = 0
            while number != 0:
                number_digit += 1
                number = number // 10
            return number_digit

        res = 0
        for num in nums:
            if get_number_digit(num) % 2 == 0:
                res += 1

        return res



if __name__ == "__main__":
    nums = [555,901,482,1771]
    solution = Solution()
    print(solution.findNumbers(nums))