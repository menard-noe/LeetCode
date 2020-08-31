from typing import List
import re


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        dico = dict()

        A = str.split(A)
        B = str.split(B)

        for char in A:
            dico[char] = dico.get(char, 0) + 1
        for char in B:
            dico[char] = dico.get(char, 0) + 1

        res = []
        for key in dico:
            if dico[key] == 1:
                res.append(key)
        return res


if __name__ == "__main__":
    # execute only if run as a script
    A = "this apple is sweet"
    B = "this apple is sour"
    solution = Solution()
    print(solution.uncommonFromSentences(A, B))