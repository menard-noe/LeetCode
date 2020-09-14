from typing import List


class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 0:
            return 0

        prev = s[0]
        current = 1
        max_val = current
        for i in range(1, len(s)):
            if s[i] == prev:
                current += 1
            else:
                max_val = max(max_val, current)
                current = 1
                prev = s[i]
        max_val = max(max_val, current)
        return max_val



if __name__ == "__main__":
    s = "cc"
    solution = Solution()
    print(solution.maxPower(s))