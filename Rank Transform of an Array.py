from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr2 = sorted(arr)
        dico = dict()

        prev = -1
        rank = 0
        for num in arr2:
            if num != prev:
                rank += 1
                prev = num
            dico[num] = rank

        for i in range(len(arr)):
            arr[i] = dico[arr[i]]
        return arr


if __name__ == "__main__":
    arr = [40,10,20,30]
    solution = Solution()
    print(solution.arrayRankTransform(arr))
