from typing import List


class Solution:
    def convertToTitle(self, n: int) -> str:
        result = ""
        alphabets = 'ZABCDEFGHIJKLMNOPQRSTUVWXY'
        alphabets = list(alphabets)

        while n > 0:
            d = n % 26
            result = alphabets[d] + result

            n = n // 26
            if d == 0:
                break

        return result


if __name__ == "__main__":
    # execute only if run as a script
    input = 27
    solution = Solution()
    print(solution.convertToTitle(input))




