from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:

            j = 1

            for i in range(0,len(A), 2):
                if A[i] % 2:
                    while A[j] % 2:
                        j += 2
                    A[i], A[j] = A[j], A[i]
            return A


if __name__ == "__main__":
    # execute only if run as a script
    input = [3,1,2,4]
    solution = Solution()
    print(solution.sortArrayByParityII(input))
