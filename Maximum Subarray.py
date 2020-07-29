from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        local_max = nums[0]
        global_max = nums[0]

        for i in range(1, len(nums)):
            local_max = max(local_max + nums[i], nums[i])
            global_max = max(local_max, global_max)
        return global_max


if __name__ == "__main__":
    # execute only if run as a script
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    solution = Solution()
    print(solution.maxSubArray(nums))