from typing import List


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        group = []

        prev = None
        length = 0

        for char in s:
            if prev is None or prev == char:
                length += 1
            else:
                group.append(length)
                length = 1
            prev = char

        group.append(length)

        res = 0

        for i in range(1, len(group)):
            res += min(group[i-1], group[i])
        return res


if __name__ == "__main__":
    # execute only if run as a script
    nums = "00110011"
    solution = Solution()
    print(solution.countBinarySubstrings(nums))