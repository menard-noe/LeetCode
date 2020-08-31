from typing import List


class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        return not (rec1[2] <= rec2[0] or
                    rec1[3] <= rec2[1] or
                    rec1[0] >= rec2[2] or
                    rec1[1] >= rec2[3])


if __name__ == "__main__":
    # execute only if run as a script
    rec1 = [0, 0, 2, 2]
    rec2 = [1, 1, 3, 3]
    solution = Solution()
    print(solution.isRectangleOverlap(rec1, rec2))
