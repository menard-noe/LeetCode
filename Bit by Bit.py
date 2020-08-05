import math


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret

if __name__ == "__main__":
    # execute only if run as a script
    input = "00000010100101000001111010011100"
    solution = Solution()
    print(solution.reverseBits(int(input,2)))