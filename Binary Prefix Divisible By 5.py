from typing import List


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        binary_num = 0

        for num in A:
            binary_num = binary_num * 2 + num
            if binary_num % 5 == 0:
                res.append(True)
            else:
                res.append(False)

        return res


if __name__ == "__main__":
    # execute only if run as a script
    input = [0,1,1]
    solution = Solution()
    print(solution.prefixesDivBy5(input))