class Solution:
    def isHappy(self, n: int) -> bool:
        dico = dict()

        def utils(n: int) -> int:
            res = 0
            while n != 0:
                rest = n % 10
                res += (rest * rest)
                n = n // 10
            return res

        while n not in dico:
            dico[n] = 1
            n = utils(n)
            if n == 1:
                return True
        return False

if __name__ == "__main__":
    # execute only if run as a script
    input = 19
    solution = Solution()
    print(solution.isHappy(input))
