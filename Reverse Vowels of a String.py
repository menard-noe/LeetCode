# Definition for singly-linked list.
from typing import List


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        v = []

        for i, x in enumerate(s):
            if x in vowel:
                v.append(i)

        s = list(s)  # turn a string into a list
        n = len(v)
        for i in range(n // 2):
            s[v[i]], s[v[n - 1 - i]] = s[v[n - 1 - i]], s[v[i]]

        return "".join(s)


if __name__ == "__main__":
    # execute only if run as a script
    input = "hello"
    solution = Solution()
    print(solution.reverseVowels(input))