from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        max_val = 0
        max_char = arr[0]
        current_val = 1
        current_char = arr[0]

        for i in range(0, len(arr) - 1):
            if arr[i] == arr[i + 1] and arr[i + 1] == current_char:
                current_val += 1
            else:
                if current_val > max_val:
                    max_val = current_val
                    max_char = current_char
                current_val = 1
                current_char = arr[i + 1]

        if current_val > max_val:
            max_val = current_val
            max_char = current_char
        return max_char


if __name__ == "__main__":
    # execute only if run as a script
    arr = [1,2,3,3]
    solution = Solution()
    print(solution.findSpecialInteger(arr))