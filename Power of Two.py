from typing import List


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        res = 1
        while res <= n:
            if res == n:
                return True
            res *= 2
        return False



if __name__ == "__main__":
    # execute only if run as a script
    nums = 17
    solution = Solution()
    print(solution.isPowerOfTwo(nums))


