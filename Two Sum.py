from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        '''Too slow'''
        """for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                res = nums[i] + nums[j]
                if res == target:
                    return [i, j]
        return None"""

        dico = dict({})
        for i in range(len(nums)):
            dico[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in dico and i != dico[target - nums[i]]:
                return [i, dico[target - nums[i]]]
        return []



if __name__ == "__main__":
    # execute only if run as a script
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    print(solution.twoSum(nums, target))