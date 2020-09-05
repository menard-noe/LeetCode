import math
from typing import List


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        nums = list(A)

        if len(nums) < 3:
            return 0
        nums = sorted(nums)
        nums.reverse()

        for i in range(0, len(nums) - 2):
            if nums[i + 1] + nums[i + 2] > nums[i]:
                return nums[i + 1] + nums[i + 2] + nums[i]

        return 0


if __name__ == "__main__":
    # execute only if run as a script
    input = [3,6,2,3]
    solution = Solution()
    print(solution.largestPerimeter(input))