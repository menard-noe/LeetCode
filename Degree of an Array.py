from typing import List


# Definition for singly-linked list.
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dico = dict()
        listMax = []

        dico_min_index = dict()
        dico_max_index = dict()

        for i, num in enumerate(nums):
            dico[num] = dico.get(num, 0) + 1
            dico_max_index[num] = i
            if num not in dico_min_index:
                dico_min_index[num] = i

        min_val = 999999
        max = 0

        for key in dico:
            if dico[key] >= max:
                if dico[key] > max:
                    min_val = 999999
                max = dico[key]
                size = dico_max_index[key] - dico_min_index[key]
                min_val = min(min_val, size)
        return min_val + 1


if __name__ == "__main__":
    # execute only if run as a script
    nums = [1,2,2,3,1,4,2]
    solution = Solution()
    print(solution.findShortestSubArray(nums))




