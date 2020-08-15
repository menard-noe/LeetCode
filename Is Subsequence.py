from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0
        t_index = 0

        while s_index != len(s):
            if t_index >= len(t):
                return False

            if s[s_index] == t[t_index]:
                s_index += 1
                t_index += 1
            else:
                t_index += 1
        return True


if __name__ == "__main__":
    # execute only if run as a script
    s = "axc"
    t = "ahbgdc"
    solution = Solution()
    print(solution.isSubsequence(s, t))