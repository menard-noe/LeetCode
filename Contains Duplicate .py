import math
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dico = dict()
        for num in nums:
            if num in dico:
                return True
            else:
                dico[num] = 0
        return False


if __name__ == "__main__":
    # execute only if run as a script
    input = [1,2,3,3]
    solution = Solution()
    print(solution.containsDuplicate(input))