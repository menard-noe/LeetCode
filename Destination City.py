from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        departs = dict()
        arrivals = dict()

        for path in paths:
            depart = path[0]
            arrival = path[1]
            departs[depart] = 1

            if arrival not in departs:
                arrivals[arrival] = 1

            if depart in arrivals:
                arrivals.pop(depart)

        return next(iter(arrivals.keys()))


if __name__ == "__main__":
    paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    solution = Solution()
    print(solution.destCity(paths))