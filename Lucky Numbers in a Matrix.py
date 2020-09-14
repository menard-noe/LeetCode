from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        dico = dict()

        for row in matrix:
            index_min = -1
            min_row = float("inf")
            for j, val in enumerate(row):
                if val < min_row:
                    min_row = val
                    index_min = j
            temp = dico.get(index_min, [])
            temp.append(min_row)
            dico[index_min] = temp

        res = []

        for j in range(len(matrix[0])):
            max_column = - float("inf")
            for row in matrix:
                max_column = max(max_column, row[j])
            if j in dico and max_column in dico[j]:
                res.append(max_column)

        return res


if __name__ == "__main__":
    matrix = [[3,7,8],[9,11,13],[15,16,17]]
    solution = Solution()
    print(solution.luckyNumbers(matrix))