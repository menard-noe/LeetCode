import copy
from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for word in words:
            temp = list(words)
            temp.remove(word)

            for word2 in temp:
                if word in word2:
                    res.append(word)
                    break

        return res


if __name__ == "__main__":
    words = ["mass","as","hero","superhero"]
    solution = Solution()
    print(solution.stringMatching(words))