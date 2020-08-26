import math
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dico = dict()

        min = 9999999
        res = []

        for i, elem in enumerate(list1):
            dico[elem] = i
        for i, elem in enumerate(list2):
            if elem in dico:
                temp = i + dico[elem]
                if temp == min:
                    res.append(elem)
                elif temp < min:
                    min = temp
                    res.clear()
                    res.append(elem)
        return res


if __name__ == "__main__":
    # execute only if run as a script
    l1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    l2 = ["KFC", "Shogun", "Burger King"]
    solution = Solution()
    print(solution.findRestaurant(l1, l2))