from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle

        if left <= len(nums) - 1:
            if nums[left] == target:
                return left

        return -1


if __name__ == "__main__":
    # execute only if run as a script
    # execute only if run as a script
    nums = [-1,0,3,5,9,12]
    target = 13

    solution = Solution()
    print(solution.search(nums, target))