from typing import List


class Solution:
    def countOdds(self, low, high):
        return int((high - low) / 2 + ((low | high) & 1))

if __name__ == "__main__":
    # execute only if run as a script
    low = 8
    high = 10
    solution = Solution()
    print(solution.countOdds(low, high))