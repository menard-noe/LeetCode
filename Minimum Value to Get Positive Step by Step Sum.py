import copy
from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        res = 1
        total_sum = res
        for num in nums:
            total_sum += num
            if total_sum <= 0:
                res += abs(total_sum) + 1
                total_sum += abs(total_sum) + 1

        return res


if __name__ == "__main__":
    nums = [1,2]
    solution = Solution()
    print(solution.minStartValue(nums))