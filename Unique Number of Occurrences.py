from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dico = dict()

        for val in arr:
            dico[val] = dico.get(val, 0) + 1

        l = []

        for key in dico:
            if dico[key] in l:
                return False
            else:
                l.append(dico[key])

        return True


if __name__ == "__main__":
    arr = [1,2,2,1,1,3]
    solution = Solution()
    print(solution.uniqueOccurrences(arr))


