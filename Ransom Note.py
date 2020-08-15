from typing import List


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dico = dict()

        for char in magazine:
            dico[char] = dico.get(char, 0) + 1

        for char in ransomNote:
            if char in dico and dico[char] > 0:
                dico[char] -= 1
            else:
                return False
        return True


if __name__ == "__main__":
    # execute only if run as a script
    ransomNote = "a"
    magazine = "bbbbacfdd"
    solution = Solution()
    print(solution.canConstruct(ransomNote, magazine))




