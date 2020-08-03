from typing import List
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^A-Za-z0-9]', '', s).lower()
        for i in range(0, len(s)//2):
            if s[i] != s[-i - 1]:
                return False
        return True



if __name__ == "__main__":
    # execute only if run as a script
    input = ""
    solution = Solution()
    print(solution.isPalindrome(input))