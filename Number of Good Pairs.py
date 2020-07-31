import math
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dico = dict()
        result = 0

        for i in nums:
            if i in dico:
                result += dico[i]
                dico[i] += 1
            else:
                dico[i] = 1

        return result


if __name__ == "__main__":
    # execute only if run as a script
    nums = [1,2,3]
    solution = Solution()
    print(solution.numIdenticalPairs(nums))