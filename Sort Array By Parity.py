from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:

            i = 0
            j = len(A) - 1

            while i < j:
                if A[i] % 2 > A[j] % 2:
                    A[i], A[j] = A[j], A[i]

                if A[i] % 2 == 0:
                    i += 1
                if A[j] % 2 == 1:
                    j -= 1


            return A


if __name__ == "__main__":
    # execute only if run as a script
    input = [3,1,2,4]
    solution = Solution()
    print(solution.sortArrayByParity(input))
