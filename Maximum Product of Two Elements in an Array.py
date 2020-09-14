from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max = 0
        second_max = 0

        for val in nums:
            if val > max:
                second_max = max
                max = val
            elif val > second_max:
                second_max = val

        return (max - 1) * (second_max - 1)


if __name__ == "__main__":
    nums = [3, 4, 5, 2]
    solution = Solution()
    print(solution.maxProduct(nums))