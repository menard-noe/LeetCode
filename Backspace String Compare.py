import collections
import itertools


class Solution(object):
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        for x, y in itertools.zip_longest(F(S), F(T)):
            if x != y:
                return False
        return True


class Solution2:
    def backspaceCompare(self, S: str, T: str) -> bool:
        a, A = [collections.deque(), collections.deque()], [S, T]
        for i in range(2):
            for j in A[i]:
                if j != '#':
                    a[i].append(j)
                elif a[i]:
                    a[i].pop()
        return a[0] == a[1]


if __name__ == "__main__":
    # execute only if run as a script
    S = "ad#c"
    T = "ad#c"
    solution = Solution2()
    print(solution.backspaceCompare(S, T))
