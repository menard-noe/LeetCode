from typing import List
from functools import cmp_to_key


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        dico = dict()

        for i, val in enumerate(arr2):
            dico[val] = i

        def cmp_items(a, b):
            if a in dico and b in dico:
                if dico[a] < dico[b]:
                    return -1
                elif dico[a] == dico[b]:
                    return 0
                else:
                    return 1

            if a in dico:
                return -1

            if b in dico:
                return 1

            if a > b:
                return 1
            elif a == b:
                return 0
            else:
                return -1

        res = sorted(arr1, key=cmp_to_key(cmp_items))
        return res


if __name__ == "__main__":
    # execute only if run as a script
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    solution = Solution()
    print(solution.relativeSortArray(arr1, arr2))




