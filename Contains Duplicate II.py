import math
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dico = dict()
        for i, num in enumerate(nums):
            if num in dico and i - dico[num] <= k :
                return True
            else:
                dico[num] = i
        return False


if __name__ == "__main__":
    # execute only if run as a script
    input = [1,2,3,1]
    k = 2
    solution = Solution()
    print(solution.containsNearbyDuplicate(input, k))