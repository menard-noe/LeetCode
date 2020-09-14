from typing import List


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        i = 0
        j = 0

        while i < len(name) and j < len(typed):
            if typed[j] == name[i]:
                prev = name[i]
                i += 1
                j += 1
            elif typed[j] == typed[j - 1]:
                j += 1
            else:
                return False

        if i != len(name):
            return False

        while j != len(typed):
            if typed[j] != typed[j - 1]:
                return False
            j += 1

        return True


if __name__ == "__main__":
    # execute only if run as a script
    name = "alex"
    typed = "aaleexx"
    solution = Solution()
    print(solution.isLongPressedName(name, typed))
