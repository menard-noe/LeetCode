from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        disctinct_number = 0
        for i in range(1, len(nums)):
            if not nums[i] == nums[disctinct_number]:
                disctinct_number += 1
                nums[disctinct_number] = nums[i]
        disctinct_number += 1
        return disctinct_number


if __name__ == "__main__":
    # execute only if run as a script
    nums = [1,1,2]
    solution = Solution()
    print(solution.removeDuplicates(nums))




