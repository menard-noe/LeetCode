
class Solution:
    def maximum69Number(self, num: int) -> int:
        temp_res = []

        while num != 0:
            temp_res.append(num % 10)
            num = num // 10

        temp_res.reverse()
        res = 0
        modif = False
        for val in temp_res:
            if val == 6 and not modif:
                res = res * 10 + 9
                modif = True
            else:
                res = res * 10 + val

        return res


if __name__ == "__main__":
    num = 669
    solution = Solution()
    print(solution.maximum69Number(num))
