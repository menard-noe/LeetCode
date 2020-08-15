from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        temp = 0
        for num in nums:
            if num == 1:
                temp += 1
            else:
                if temp > res:
                    res = temp
                temp = 0
        if temp > res:
            res = temp
        return res


if __name__ == "__main__":
    # execute only if run as a script
    nums = [1,1,0,1,1,1,0,1,1,1,1,1,1]
    solution = Solution()
    print(solution.findMaxConsecutiveOnes(nums))