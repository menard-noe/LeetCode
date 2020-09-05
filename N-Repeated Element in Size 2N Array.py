import math
from typing import List


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        for k in range(1, 4):
            for i in range(len(A) - k):
                if A[i] == A[i+k]:
                    return A[i]


if __name__ == "__main__":
    # execute only if run as a script
    nums = [1,2,3,3]
    solution = Solution()
    print(solution.repeatedNTimes(nums))