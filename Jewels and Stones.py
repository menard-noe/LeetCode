from typing import List


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        dico = dict()

        for char in J:
            dico[char] = 1

        res = 0
        for char in S:
            if char in dico:
                res += 1

        return res



if __name__ == "__main__":
    # execute only if run as a script
    J = "aA"
    S = "aAAbbbb"
    solution = Solution()
    print(solution.numJewelsInStones(J, S))