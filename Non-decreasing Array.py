from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        wrongplace = None

        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if wrongplace is None:
                    wrongplace = i
                else:
                    return False

        return (wrongplace is None or wrongplace == 0 or wrongplace == len(nums) - 2 or
                nums[wrongplace - 1] <= nums[wrongplace + 1] or nums[wrongplace] <= nums[wrongplace + 2])


if __name__ == "__main__":
    # execute only if run as a script
    nums = [4, 2, 3]
    solution = Solution()
    print(solution.checkPossibility(nums))