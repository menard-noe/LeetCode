import math


class Solution:
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        if not str:
            return False

        ss = (str + str)[1:-1]
        return ss.find(str) != -1


if __name__ == "__main__":
    # execute only if run as a script
    Input = "abab"
    solution = Solution()
    print(solution.repeatedSubstringPattern(Input))

