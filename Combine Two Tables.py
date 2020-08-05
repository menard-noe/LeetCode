import math


class Solution:
    def climbStairs(self, n: int) -> int:
        dico_memo_stairs = dict({})
        return self.recu_stair(0, n, dico_memo_stairs)

    def recu_stair(self, current_stair, final_stair, dico_memo_stairs):
        if current_stair > final_stair:
            return 0
        elif current_stair == final_stair:
            return 1
        elif dico_memo_stairs.get(current_stair):
            return dico_memo_stairs[current_stair]
        else:
            dico_memo_stairs[current_stair] = self.recu_stair(current_stair + 1, final_stair, dico_memo_stairs) + self.recu_stair(current_stair + 2, final_stair, dico_memo_stairs)
            return dico_memo_stairs[current_stair]

if __name__ == "__main__":
    # execute only if run as a script
    input = 4
    solution = Solution()
    print(solution.climbStairs(input))