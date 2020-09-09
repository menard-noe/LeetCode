from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        word_count = []
        dico_chars = dict()

        for word in words:
            dico = dict()
            for char in word:
                dico[char] = dico.get(char, 0) + 1
            word_count.append(dico)

        for char in chars:
            dico_chars[char] = dico_chars.get(char, 0) + 1

        res = 0
        index = 0
        for word in word_count:
            for key in word:
                if key not in dico_chars or word[key] > dico_chars[key]:
                    index += 1
                    break
            else:
                res += len(words[index])
                index += 1
        return res


if __name__ == "__main__":
    # execute only if run as a script
    words = ["hello","world","leetcode"]
    chars = "welldonehoneyr"
    solution = Solution()
    print(solution.countCharacters(words,chars))




