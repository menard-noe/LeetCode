from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dico = dict()
        for song in time:
            modulo = song % 60
            dico[modulo] = dico.get(modulo, 0) + 1

        res = 0
        for key in dico:
            if 60 - key in dico and dico[key] > 0 and dico[60 - key] > 0:
                if 60 - key != key:
                    res += (dico[key] * dico[60 - key]) / 2
                else:
                    res += ((dico[key] - 1) * ((dico[key] - 1) + 1)) / 2

        if 0 in dico:
            res += ((dico[0] - 1) * ((dico[0] - 1) + 1)) / 2
        return int(res)


if __name__ == "__main__":
    # execute only if run as a script
    input = [60,60,60]
    solution = Solution()
    print(solution.numPairsDivisibleBy60(input))