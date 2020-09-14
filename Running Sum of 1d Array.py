from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cumulative_sum = 0
        for i in range(len(nums)):
            cumulative_sum += nums[i]
            nums[i] = cumulative_sum

        return nums


if __name__ == "__main__":
    nums = [1,2,3,4]
    solution = Solution()
    print(solution.runningSum(nums))