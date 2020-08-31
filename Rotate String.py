
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return B in A + A and len(A) == len(B)


if __name__ == "__main__":
    # execute only if run as a script
    A = ""
    B = ""
    solution = Solution()
    print(solution.rotateString(A, B))
