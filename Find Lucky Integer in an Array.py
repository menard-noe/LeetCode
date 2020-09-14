from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dico = dict()
        res = -1

        for val in arr:
            dico[val] = dico.get(val, 0) + 1

        for key in dico:
            if dico[key] == key:
                res = max(res, key)

        return res


if __name__ == "__main__":
    arr = [2,2,3,3,3,4]
    solution = Solution()
    print(solution.findLucky(arr))