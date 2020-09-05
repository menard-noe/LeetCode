from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1

        dico_trust_from_other = dict()
        dico_trust_someone = dict()

        for val in trust:
            truster = val[0]
            trusted = val[1]
            dico_trust_someone[truster] = True
            dico_trust_from_other[trusted] = dico_trust_from_other.get(trusted, 0) + 1

        for key in dico_trust_from_other:
            if dico_trust_from_other[key] == N - 1 and key not in dico_trust_someone:
                return key

        return -1


if __name__ == "__main__":
    # execute only if run as a script
    N = 4
    trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
    solution = Solution()
    print(solution.findJudge(N, trust))




