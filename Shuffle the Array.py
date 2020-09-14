from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n, 2 * n):
            nums[i] = (nums[i] * 10000) + nums[i - n]

        for i in range(n, 2 * n):
            nums[(i - n) * 2] = nums[i] % 10000
            nums[(i - n) * 2 + 1] = nums[i] // 10000

        return nums

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7,8,9,10,11,12]
    n = 6
    solution = Solution()
    print(solution.shuffle(nums, n))