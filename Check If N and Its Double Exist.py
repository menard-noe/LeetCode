from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dico = dict()

        for val in arr:
            if val / 2 in dico or val * 2 in dico:
                return True
            else:
                dico[val] = 1

        return False


if __name__ == "__main__":
    arr = [10,2,5,3]
    solution = Solution()
    print(solution.checkIfExist(arr))