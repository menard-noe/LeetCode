from typing import List


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dico = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}

        for char in text:
            dico[char] = dico.get(char, 0) + 1

        min_balloons = 999999

        min_balloons = min(min_balloons, dico['b'])
        min_balloons = min(min_balloons, dico['a'])
        min_balloons = min(min_balloons, dico['l'] // 2)
        min_balloons = min(min_balloons, dico['o'] // 2)
        min_balloons = min(min_balloons, dico['n'])
        return min_balloons


if __name__ == "__main__":
    text = "leetcode"
    solution = Solution()
    print(solution.maxNumberOfBalloons(text))


