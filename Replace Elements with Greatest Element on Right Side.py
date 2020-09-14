from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest_right = arr[-1]
        arr[-1] = -1

        for i in range(len(arr) - 2, -1, -1):
            temp = arr[i]
            arr[i] = greatest_right
            greatest_right = max(temp, greatest_right)
        return arr


if __name__ == "__main__":
    arr = [17,18,5,4,6,1]
    solution = Solution()
    print(solution.replaceElements(arr))