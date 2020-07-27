from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        if len(haystack) == len(needle) and haystack == needle:
            return 0

        for i in range(0, len(haystack) - (len(needle) - 1)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

if __name__ == "__main__":
    # execute only if run as a script
    haystack = "abc"
    needle = "c"
    solution = Solution()
    print(solution.strStr(haystack, needle))




