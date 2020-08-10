from typing import List
import re


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dico_s = dict()
        dico_t = dict()

        for char in s:
            if char in dico_s:
                dico_s[char] += 1
            else:
                dico_s[char] = 1
        for char in t:
            if char in dico_t:
                dico_t[char] += 1
            else:
                dico_t[char] = 1

        if len(dico_s) != len(dico_t):
            return False
        for key in dico_s:
            if key not in dico_t or dico_s[key] != dico_t[key]:
                return False
        return True


if __name__ == "__main__":
    # execute only if run as a script
    s = "rat"
    t = "car"
    solution = Solution()
    print(solution.isAnagram(s, t))