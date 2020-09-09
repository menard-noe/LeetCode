from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        min_val = 99999
        for i in range(0, len(arr) - 1):
            min_val = min(min_val, abs(arr[i + 1] - arr[i]))

        dico = dict()
        for val in arr:
            dico[val] = 1

        res = []
        for val in arr:
            if val + min_val in dico and val < (val + min_val):
                res.append((val, val + min_val))

        return res


if __name__ == "__main__":
    arr = [4,2,1,3]
    solution = Solution()
    print(solution.minimumAbsDifference(arr))


