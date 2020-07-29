from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0 or target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)

        for i in range(0, len(nums)):
            if target <= nums[i]:
                return i
        return -1





if __name__ == "__main__":
    # execute only if run as a script
    nums = [1,3,5,6]
    target = 0
    solution = Solution()
    print(solution.searchInsert(nums, target))