from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:

        dico_target = dict()
        dico_arr = dict()

        for num in target:
            dico_target[num] = dico_target.get(num, 0) + 1
        for num in arr:
            dico_arr[num] = dico_arr.get(num, 0) + 1

        if len(dico_target) == len(dico_arr):
            for key in dico_target.keys():
                if key not in dico_arr or dico_target[key] != dico_arr[key]:
                    return False
        else:
            return False
        return True


if __name__ == "__main__":
    target = [1, 2, 3, 4]
    arr = [2, 4, 1, 3]
    solution = Solution()
    print(solution.canBeEqual(target, arr))