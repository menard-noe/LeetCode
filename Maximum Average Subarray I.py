from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        sum = 0

        for val in nums[0:k]:
            sum += val

        temp = sum
        for i in range(k, len(nums)):
            temp = temp + nums[i] - nums[i - k]
            if temp > sum:
                sum = temp
        return sum / k



if __name__ == "__main__":
    # execute only if run as a script
    nums = [0,4,0,3,2]
    k = 1
    solution = Solution()
    print(solution.findMaxAverage(nums, k))