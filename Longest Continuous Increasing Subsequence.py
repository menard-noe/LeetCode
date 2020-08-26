from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        prev = nums[0]
        max = 1
        current = 1
        for i in range(1, len(nums)):
            if nums[i] <= prev:
                if max < current:
                    max = current
                current = 0
            prev = nums[i]
            current += 1

        if max < current:
            max = current
        return max

if __name__ == "__main__":
    # execute only if run as a script
    input = [1,2,3,7,4]
    solution = Solution()
    print(solution.findLengthOfLCIS(input))
