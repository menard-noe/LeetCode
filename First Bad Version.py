class Solution:
    # The isBadVersion API is already defined for you.
    # @param version, an integer
    # @return an integer
    def __init__(self):
        self.dico = dict()
        for i in range(0, 5):
            self.dico[i] = False
        for i in range(5, 9):
            self.dico[i] = True

    def isBadVersion(self, version):
        return self.dico[version - 1]

    def firstBadVersion(self, n):

        left = 1
        right = n
        while left != right:
            mid = (left + right) // 2
            version = self.isBadVersion(mid)
            if version:
                right = mid
            else:
                left = mid + 1
        return right


if __name__ == "__main__":
    # execute only if run as a script
    input = 10
    solution = Solution()
    print(solution.firstBadVersion(input))
