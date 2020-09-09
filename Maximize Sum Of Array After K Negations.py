from typing import List


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A = sorted(A)
        val_min = float("inf")

        res = 0

        for i, val in enumerate(A):
            if val < 0 < K:
                val = -val
                K -= 1
            elif val == 0:
                K = 0
            elif val > 0 and K > 0:
                if K % 2 == 1:
                    if val >= val_min:
                        res -= val_min * 2
                    else:
                        val = -val
                K = 0
            val_min = min(val_min, val)
            res += val

        return res

if __name__ == "__main__":
    # execute only if run as a script
    A = [8,-7,-3,-9,1,9,-6,-9,3]
    K = 8
    solution = Solution()
    print(solution.largestSumAfterKNegations(A, K))