from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        left = 0
        right = len(A) - 1
        res = []

        while left <= right:
            # add case where left < 0 and right > 0 to opti algo
            if abs(A[left]) > abs(A[right]):
                res.append(A[left] * A[left])
                left += 1
            else:
                res.append(A[right] * A[right])
                right -= 1

        res.reverse()
        return res


if __name__ == "__main__":
    # execute only if run as a script
    input = [-7,-3,2,3,11]
    solution = Solution()
    print(solution.sortedSquares(input))