from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a: int, b: int):
            if a % b == 0:
                return b
            else:
                return gcd(b, a % b)

        dico = dict()

        for card in deck:
            dico[card] = dico.get(card, 0) + 1

        min = float('inf')
        for key in dico:
            if dico[key] < min:
                min = dico[key]

        for val in dico.values():
            min = gcd(min, val)
            if min == 1:
                return False
        return True


if __name__ == "__main__":
    # execute only if run as a script
    deck = [1,1,1,1,2,2,2,2,2,2]
    solution = Solution()
    print(solution.hasGroupsSizeX(deck))