from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dico = dict({})
        for i in range(len(numbers)):
            dico[numbers[i]] = i
        for i in range(len(numbers)):
            if target - numbers[i] in dico and i != dico[target - numbers[i]]:
                return [i, dico[target - numbers[i]]]
        return []

    '''def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        l = len(numbers) - 1
        while i < l:
            n = numbers[i] + numbers[l]
            if n < target:
                i += 1
            if n > target:
                l -= 1
            if n == target:
                return [i+1,l+1]'''


if __name__ == "__main__":
    # execute only if run as a script
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    print(solution.twoSum(nums, target))