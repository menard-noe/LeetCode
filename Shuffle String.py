import math
from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        if len(indices) == 0:
            return ""

        shuffled_tab = [None] * len(indices)

        for i in range(0, len(indices)):
            shuffled_tab[indices[i]] = s[i]

        shuffled__string = ""
        for char in shuffled_tab:
            shuffled__string += char
        return shuffled__string


if __name__ == "__main__":
    # execute only if run as a script
    s = ""
    indices = [4, 5, 6, 7, 0, 2, 1, 3]
    solution = Solution()
    print(solution.restoreString(s, indices))