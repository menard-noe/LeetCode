from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dico = dict()

        for num in nums:
            dico[num] = dico.get(num, 0) + 1

        res = []
        keys_sorted = sorted(dico.keys())

        val = 0
        for key in keys_sorted:
            temp = dico[key]
            dico[key] = val
            val += temp

        for num in nums:
            res.append(dico[num])

        return res


if __name__ == "__main__":
    nums = [8,1,2,2,3]
    solution = Solution()
    print(solution.smallerNumbersThanCurrent(nums))