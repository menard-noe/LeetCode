# Definition for singly-linked list.
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(0, len(s) // 2):
            s[i], s[-i - 1] = s[-i - 1], s[i]
        print(s)

if __name__ == "__main__":
    # execute only if run as a script
    input = ["h", "e", "l", "l", "o"]
    solution = Solution()
    print(solution.reverseString(input))