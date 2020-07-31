import math
from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) <= 2:
            return True
        first_min, second_min = float('inf'), float('inf')
        for n in arr:
            if n <= first_min:
                first_min, second_min = n, first_min
            elif n < second_min:
                second_min = n
        arr_prog = [first_min + (second_min - first_min) * i for i in range(len(arr))]
        for a in arr:
            if a in arr_prog:
                arr_prog.remove(a)
            else:
                return False
        return arr_prog == []

if __name__ == "__main__":
    # execute only if run as a script
    arr = [3, 5, 1]
    solution = Solution()
    print(solution.canMakeArithmeticProgression(arr))