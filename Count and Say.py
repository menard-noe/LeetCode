from typing import List


class Solution:
    def countAndSay(self, n: int) -> str:

        res = "1"
        if n == 0:
            return res

        for i in range(1, n):
            char = res[0]
            counter_same_char = 0
            temp_res = ""
            for j in range(0, len(res)):
                if char is str(res[j]):
                    counter_same_char += 1
                else:
                    temp_res += str(counter_same_char) + str(char)
                    char = res[j]
                    counter_same_char = 1
            temp_res += str(counter_same_char) + str(char)
            res = temp_res
        return res


if __name__ == "__main__":
    # execute only if run as a script
    nums = 6
    solution = Solution()
    print(solution.countAndSay(nums))