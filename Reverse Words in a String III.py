class Solution:
    def reverseWords(self, s: str) -> str:
        new_string = s.split()
        res = ""

        for index, word in enumerate(new_string):
            for i in range(0, len(word)):
                res += word[-i - 1]
            if index != len(new_string) - 1:
                res += " "
        return res


if __name__ == "__main__":
    # execute only if run as a script
    Input = "Let's take LeetCode contest"
    solution = Solution()
    print(solution.reverseWords(Input))