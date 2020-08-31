from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        self.dico = dict()

        def utils(cost: List[int], current_stair) -> int:
            if len(cost) <= current_stair:
                return 0
            else:
                next = 0
                next_next = 0
                if current_stair + 1 not in self.dico:
                    next = utils(cost, current_stair + 1)
                    self.dico[current_stair + 1] = next
                else:
                    next = self.dico[current_stair + 1]

                if current_stair + 2 not in self.dico:
                    next_next = utils(cost, current_stair + 2)
                    self.dico[current_stair + 2] = next_next
                else:
                    next_next = self.dico[current_stair + 2]

                return min(next, next_next) + cost[current_stair]

        return min(utils(cost, 0), utils(cost, 1))


if __name__ == "__main__":
    # execute only if run as a script
    solution = Solution()
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(solution.minCostClimbingStairs(cost))
