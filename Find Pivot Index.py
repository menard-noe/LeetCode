from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        sum_array = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            if left_sum == (sum_array - (left_sum + num)):
                return i
            else:
                left_sum += num

        return -1


if __name__ == "__main__":
    # execute only if run as a script
    nums = [1, 7, 3, 6, 5, 6]
    solution = Solution()
    print(solution.pivotIndex(nums))
