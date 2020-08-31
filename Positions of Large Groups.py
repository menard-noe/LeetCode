from typing import List


class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        counter = 0
        prev = ""
        res = []

        for i, char in enumerate(S):
            if char == prev:
                counter += 1
            else:
                if counter >= 3:
                    res.append([i - counter, i - 1])
                prev = char
                counter = 1

        if counter >= 3:
            res.append([len(S) - counter, len(S) - 1])
        return res


if __name__ == "__main__":
    # execute only if run as a script
    input = "abcdddeeeeaabbbcd"
    solution = Solution()
    print(solution.largeGroupPositions(input))


