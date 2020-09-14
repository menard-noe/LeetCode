from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        res = 0

        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                res += 1

        return res


if __name__ == "__main__":
    startTime = [1,2,3]
    endTime = [3,2,7]
    queryTime = 4
    solution = Solution()
    print(solution.busyStudent(startTime, endTime, queryTime))