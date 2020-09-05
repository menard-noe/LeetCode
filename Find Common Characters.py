from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        from collections import Counter
        c=A[0]
        for i in range(1,len(A)):
            c = list((Counter(c) & Counter(A[i])).elements())
        return c


if __name__ == "__main__":
    # execute only if run as a script
    input = ["cool","lock","cook"]
    solution = Solution()
    print(solution.commonChars(input))




