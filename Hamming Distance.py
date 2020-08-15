class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
            return bin(x ^ y).count("1")


if __name__ == "__main__":
    # execute only if run as a script
    x = 1
    y = 4
    solution = Solution()
    print(solution.hammingDistance(x, y))
