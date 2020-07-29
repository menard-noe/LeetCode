from typing import List

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0

        i = len(s) - 1
        got_a_word = False
        index_before_word = 0

        while i >= 0:
            if s[i] == " ":
                if got_a_word:
                    return (len(s) - 1) - i - index_before_word
                else:
                    index_before_word += 1
            else:
                got_a_word = True
            i -= 1

        if got_a_word:
            return len(s) - index_before_word
        else:
            return 0


if __name__ == "__main__":
    # execute only if run as a script
    input = "Hello Worlddd "
    solution = Solution()
    print(solution.lengthOfLastWord(input))