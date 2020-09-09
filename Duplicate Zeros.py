from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        cum_zero = []

        sum_zero = 0
        for val in arr:
            cum_zero.append(sum_zero)
            if val == 0:
                sum_zero += 1

        for i in range(len(arr) - 1, -1, -1):
            new_index = i + cum_zero.pop()
            if new_index < len(arr):
                arr[new_index] = arr[i]
                if arr[new_index] == 0 and new_index + 1 < len(arr):
                    arr[new_index + 1] = 0


if __name__ == "__main__":
    # execute only if run as a script
    input = [1, 2, 3]
    solution = Solution()
    print(solution.duplicateZeros(input))