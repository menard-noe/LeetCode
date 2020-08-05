from typing import List


class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        alphabets = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        alphabets = list(alphabets)
        map = dict(zip(alphabets, range(27)))

        for i in range(len(s)):
                res = res * 26 + map[s[i]]
        return res


if __name__ == "__main__":
    # execute only if run as a script
    input = "ZY"
    solution = Solution()
    print(solution.titleToNumber(input))




