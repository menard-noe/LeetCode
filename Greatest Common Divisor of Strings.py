from typing import List


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        min_string = min(str1, str2)
        max_string = max(str1, str2)
        res = min_string
        if min_string not in max_string:
            return ""

        while len(res) > 0:
            multiply_max = len(max_string) // len(res)
            multiply_min = len(min_string) // len(res)

            if res * multiply_max == max_string and res * multiply_min == min_string:
                return res
            else:
                res = res[0:-1]

        return ""


if __name__ == "__main__":
    # execute only if run as a script
    str1 = "AAAAA"
    str2 = "AA"
    solution = Solution()
    print(solution.gcdOfStrings(str1, str2))