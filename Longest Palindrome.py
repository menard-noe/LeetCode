from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> int:
        dico = dict()

        for char in s:
            dico[char] = dico.get(char, 0) + 1
        res = 0
        for key in dico:
            res += (dico[key] // 2) * 2

        if res < len(s):
            res += 1
        return res


if __name__ == "__main__":
    # execute only if run as a script
    Input = "abccccdd"
    solution = Solution()
    print(solution.longestPalindrome(Input))
