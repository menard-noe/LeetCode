from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) is 0:
            return ""

        common_prefix = strs[0]

        for i in range(1, len(strs)):
            common_prefix = self.comparator(common_prefix, strs[i])
        return common_prefix

    @staticmethod
    def comparator(a: str, b: str):
        count = 0
        for i in range(len(a)):
            if len(b) > i and a[i] == b[i]:
                count += 1
            else:
                break
        return a[:count]


if __name__ == "__main__":
    # execute only if run as a script
    Input = ["flower","flow","flight"]
    solution = Solution()
    print(solution.longestCommonPrefix(Input))
