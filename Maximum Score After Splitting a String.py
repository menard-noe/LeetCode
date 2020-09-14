
class Solution:
    def maxScore(self, s: str) -> int:
        res = - float("inf")

        number_one = s.count("1")
        number_zero = 0

        for i, char in enumerate(s):
            if char == '0':
                number_zero += 1
            else:
                number_one -= 1
            if i != len(s) - 1:
                res = max(res, number_one + number_zero)

        return res


if __name__ == "__main__":
    s = "00"
    solution = Solution()
    print(solution.maxScore(s))