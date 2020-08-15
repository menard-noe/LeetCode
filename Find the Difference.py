import collections
from typing import List


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        count_s = collections.Counter(s)
        count_t = collections.Counter(t)

        for key in count_t:
            if key not in count_s or count_s[key] != count_t[key]:
                return key


if __name__ == "__main__":
    # execute only if run as a script
    s = "abcd"
    t = "abcde"
    solution = Solution()
    print(solution.findTheDifference(s, t))
