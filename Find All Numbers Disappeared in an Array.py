import collections
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            a = abs(n) - 1
            if nums[a] > 0: nums[a] *= -1
        return [i+1 for i in range(len(nums)) if nums[i] > 0]


if __name__ == "__main__":
    # execute only if run as a script
    s = [4,3,2,7,8,2,3,1]
    solution = Solution()
    print(solution.findDisappearedNumbers(s))
