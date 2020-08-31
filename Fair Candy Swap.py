from typing import List


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        Sa = sum(A)
        Sb = sum(B)
        setB = set(B)
        for x in A:
            if x + (Sb - Sa) / 2 in setB:
                return [x, x + (Sb - Sa) / 2]


if __name__ == "__main__":
    # execute only if run as a script
    A = [1, 1]
    B = [2, 2]
    solution = Solution()
    print(solution.fairCandySwap(A, B))




