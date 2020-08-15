import math
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(g) == 0 or len(s) == 0:
            return 0

        s.sort()
        g.sort()
        count = 0
        i = 0
        for child in g:
            if len(s) == 0:
                break
            while i < len(s):
                if s[i] >= child:
                    s.pop(i)
                    count += 1
                    break
                else:
                    i += 1
        return count


if __name__ == "__main__":
    child = [10, 9, 8, 7]
    cookie = [5, 6, 7, 8]
    solution = Solution()
    print(solution.findContentChildren(child, cookie))