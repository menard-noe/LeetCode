from typing import List

import math

import str as str


class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        map_index = {}

        words = str.split()
        if len(pattern) != len(words):
            return False

        for i in range(len(words)):
            c = pattern[i]
            w = words[i]

            char_key = 'char_{}'.format(c)
            char_word = 'word_{}'.format(w)

            if char_key not in map_index:
                map_index[char_key] = i

            if char_word not in map_index:
                map_index[char_word] = i

            if map_index[char_key] != map_index[char_word]:
                return False

        return True


if __name__ == "__main__":
    # execute only if run as a script
    pattern = "abba"
    str = "dog cat cat dog"

    solution = Solution()
    print(solution.wordPattern(pattern, str))