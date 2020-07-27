from typing import List


class Solution:
    def removeElement(self, nums, val):
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count




if __name__ == "__main__":
    # execute only if run as a script
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    solution = Solution()
    print(solution.removeElement(nums, val))




