from typing import List


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        i = 0
        d = len(S)
        res = []

        for s in S:
            if s == 'I':
                res.append(i)
                i += 1
            if s == 'D':
                res.append(d)
                d -= 1

        return res + [d]

if __name__ == "__main__":
    # execute only if run as a script
    input = "IDID"
    solution = Solution()
    print(solution.diStringMatch(input))




