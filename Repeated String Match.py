import math


class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:

        q = ((len(B) - 1) // len(A)) + 1

        for i in range(0, 2):
            if B in A * (q + i):
                return q + i

        return -1


if __name__ == "__main__":
    # execute only if run as a script
    a = "abcd"
    b = "cdabcdab"
    solution = Solution()
    print(solution.repeatedStringMatch(a, b))

