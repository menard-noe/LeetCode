import math
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index = 0
        for i, num in enumerate(nums):
            if num == 0:
                index += 1
            else:
                nums[i - index] = num
                if index > 0:
                    nums[i] = 0
        print(nums)


if __name__ == "__main__":
    # execute only if run as a script
    nums = [1,2,3]
    solution = Solution()
    print(solution.moveZeroes(nums))