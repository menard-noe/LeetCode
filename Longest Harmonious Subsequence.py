from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dico = dict()

        for num in nums:
            dico[num] = dico.get(num, 0) + 1

        res = 0
        for key in dico:
            val = dico[key]
            val_bellow = dico.get(key - 1, 0)
            val_up = dico.get(key + 1, 0)

            if val_bellow == 0:
                val_bellow = -999999999999999
            if val_up == 0:
                val_up = -9999999999
            res = max(res, val_bellow + val, val_up + val)
        return res


if __name__ == "__main__":
    # execute only if run as a script
    Input = [1,3,2,2,5,2,3,7]
    solution = Solution()
    print(solution.findLHS(Input))
