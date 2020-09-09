from typing import List


class Solution:
    def bitwiseComplement(self, N: int) -> int:

        binary = ""

        while N != 0:
            modulo = N % 2
            N = N // 2
            binary += str(modulo)

        if binary == "":
            binary = "0"

        binary = binary[::-1]

        binary_complement = ""
        for byte in binary:
            if byte == '0':
                binary_complement += '1'
            else:
                binary_complement += '0'
        binary_complement = binary_complement.lstrip("0")
        res = 0
        for i in range(len(binary_complement)):
            if binary_complement[i] == '1':
                res += pow(2, len(binary_complement) - 1 - i)

        return res


if __name__ == "__main__":
    # execute only if run as a script
    input = 5
    solution = Solution()
    print(solution.bitwiseComplement(input))