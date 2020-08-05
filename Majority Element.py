from typing import List


class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate


if __name__ == "__main__":
    # execute only if run as a script
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    solution = Solution()
    print(solution.majorityElement(nums))