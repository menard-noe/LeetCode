from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dico_alphabet = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            first = words[i]
            second = words[i + 1]

            for char_index in range(min(len(first), len(second))):
                if first[char_index] != second[char_index]:
                    if dico_alphabet[first[char_index]] > dico_alphabet[second[char_index]]:
                        return False
                    break
            else:
                if len(first) > len(second):
                    return False

        return True


if __name__ == "__main__":
    # execute only if run as a script
    words = ["hello","leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    solution = Solution()
    print(solution.isAlienSorted(words, order))