from typing import List


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        res = 1
        while res <= n:
            if res == n:
                return True
            res *= 3
        return False



if __name__ == "__main__":
    # execute only if run as a script
    nums = 9
    solution = Solution()
    print(solution.isPowerOfThree(nums))


