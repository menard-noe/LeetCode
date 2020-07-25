import math

class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        temp_x = x
        reversed_x = 0
        while x > 0:
            reversed_x = reversed_x * 10 + x % 10  # can overflow !
            x = math.floor(x / 10)

        if temp_x == reversed_x:
            return True
        else:
            return False


if __name__ == "__main__":
    # execute only if run as a script
    Input = 101
    solution = Solution()
    print(solution.isPalindrome(Input))
