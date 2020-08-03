from typing import List


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a



if __name__ == "__main__":
    # execute only if run as a script
    input = [3, 1, 2]
    solution = Solution()
    print(solution.singleNumber(input))
