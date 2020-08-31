from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dico = dict()
        dico[5] = 0
        dico[10] = 0

        for bill in bills:
            if bill == 5:
                dico[5] = dico[5] + 1
            elif bill == 10:
                if dico[5] > 0:
                    dico[5] = dico[5] - 1
                    dico[10] = dico[10] + 1
                else:
                    return False
            elif bill == 20:
                if dico[10] > 0 and dico[5] > 0:
                    dico[5] = dico[5] - 1
                    dico[10] = dico[10] - 1
                elif dico[5] >= 3:
                    dico[5] = dico[5] - 3
                else:
                    return False
        return True


if __name__ == "__main__":
    # execute only if run as a script
    input = [5,5,10,10,20]
    solution = Solution()
    print(solution.lemonadeChange(input))