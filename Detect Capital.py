from typing import List


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True

        capitals = True
        not_capitals = True
        first_capital = True

        for i, char in enumerate(word):
            if capitals or not_capitals or first_capital:
                if str.isupper(char):
                    not_capitals = False
                    if i != 0:
                        first_capital = False
                else:
                    capitals = False
            else:
                break

        return capitals or not_capitals or first_capital


if __name__ == "__main__":
    # execute only if run as a script
    input = "Fla"
    solution = Solution()
    print(solution.detectCapitalUse(input))




