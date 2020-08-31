# Definition for a binary tree node.
import math
from typing import List

class Solution(object):
    def shortestToChar(self, S, C):
        prev = float('-inf')
        ans = []
        for i, x in enumerate(S):
            if x == C: prev = i
            ans.append(i - prev)

        prev = float('inf')
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C: prev = i
            ans[i] = min(ans[i], prev - i)

        return ans


if __name__ == "__main__":
    # execute only if run as a script
    S = "loveleetcode"
    C = 'e'
    solution = Solution()
    print(solution.shortestToChar(S, C))