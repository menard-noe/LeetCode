from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) in (0, 1):
            return False

        increasing = True
        for i in range(0, len(A) - 1):
            if increasing:
                if A[i] < A[i + 1]:
                    continue
                elif A[i] == A[i + 1] or i == 0:
                    return False
                else:
                    increasing = False
            else:
                if A[i] > A[i + 1]:
                    continue
                else:
                    return False
        if not increasing:
            return True
        else:
            return False

class Solution2:
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1

        return i == N-1

if __name__ == "__main__":
    # execute only if run as a script
    input = []
    solution = Solution()
    print(solution.validMountainArray(input))