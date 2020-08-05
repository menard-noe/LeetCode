from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        i_minus_1 = 0
        i_minus_2 = 0
        i_total = 0

        for num in nums:
            i_minus_2 = i_minus_1
            i_minus_1 = i_total
            i_total = max(num + i_minus_2, i_minus_1)

        return i_total


if __name__ == "__main__":
    # execute only if run as a script
    input = [1,2,3,1]
    solution = Solution()
    print(solution.rob(input))




