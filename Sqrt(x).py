import math


class Solution:
    def mySqrt(self, x: int) -> int:

        if x < 2:
            return x

        left = 1
        right = x

        while left != right:
            middle = int(math.floor((left + right)/2))
            middle_squared = middle * middle
            if middle_squared == x:
                return middle
            elif middle_squared > x:
                right = middle
            elif middle_squared < x:
                if left == middle:
                    return left
                else:
                    left = middle

        return -1


if __name__ == "__main__":
    # execute only if run as a script
    input = 3
    solution = Solution()
    print(solution.mySqrt(input))