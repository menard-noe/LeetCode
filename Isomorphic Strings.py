from typing import List


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dico = dict()
        dico2 = dict()

        for i in range(0, len(s)):
            if s[i] in dico:
                if dico[s[i]] != t[i]:
                    return False
            elif t[i] in dico2:
                if dico2[t[i]] != s[i]:
                    return False
            else:
                dico[s[i]] = t[i]
                dico2[t[i]] = s[i]
        return True




if __name__ == "__main__":
    # execute only if run as a script
    s = "ab"
    t = "aa"
    solution = Solution()
    print(solution.isIsomorphic(s, t))