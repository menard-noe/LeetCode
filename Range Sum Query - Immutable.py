from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.dico = dict()
        self.dico[-1] = 0

        temp_addition = 0
        for i, num in enumerate(nums):
            temp_addition += num
            self.dico[i] = temp_addition

    def sumRange(self, i: int, j: int) -> int:
        return self.dico[j] - self.dico[i - 1]



if __name__ == "__main__":
    # execute only if run as a script
    nums = [-2, 0, 3, -5, 2, -1]
    i = 0
    j = 2
    solution = NumArray(nums)
    print(solution.sumRange(i, j))


