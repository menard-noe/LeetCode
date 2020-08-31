from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        i_length = len(matrix)
        j_length = len(matrix[0])

        for i in range(0, i_length):
            j_matrice = 0
            i_matrice = i

            val = matrix[i_matrice][j_matrice]
            while j_matrice < j_length and i_matrice < i_length:
                if matrix[i_matrice][j_matrice] != val:
                    return False
                j_matrice += 1
                i_matrice += 1

        for j in range(0, j_length):
            j_matrice = j
            i_matrice = 0

            val = matrix[i_matrice][j_matrice]
            while j_matrice < j_length and i_matrice < i_length:
                if matrix[i_matrice][j_matrice] != val:
                    return False
                j_matrice += 1
                i_matrice += 1

        return True


if __name__ == "__main__":
    # execute only if run as a script
    matrix = [
        [1, 2],
        [2, 2]
    ]
    solution = Solution()
    print(solution.isToeplitzMatrix(matrix))
