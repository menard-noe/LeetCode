from typing import List


class Solution:

    def minTimeToVisitAllPoints2(self, points: List[List[int]]) -> int:
        steps = 0
        for i in range(len(points) - 1):
            point = points[i]
            next_point = points[i + 1]
            steps += max(abs(next_point[0] - point[0]), abs(next_point[1] - point[1]))
        return steps

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
            x = points[0][0]
            y = points[0][1]
            sec = 0

            for point in points:
                x_point = point[0]
                y_point = point[1]
                while x != x_point or y != y_point:
                    if x > x_point and y > y_point:
                        x -= 1
                        y -= 1
                    elif x > x_point and y < y_point:
                        x -= 1
                        y += 1
                    elif x < x_point and y < y_point:
                        x += 1
                        y += 1
                    elif x < x_point and y > y_point:
                        x += 1
                        y -= 1
                    elif x > x_point and y == y_point:
                        x -= 1
                    elif x < x_point and y == y_point:
                        x += 1
                    elif x == x_point and y < y_point:
                        y += 1
                    elif x == x_point and y > y_point:
                        y -= 1
                    sec += 1

            return sec


if __name__ == "__main__":
    points = [[1, 1], [3, 4], [-1, 0]]
    solution = Solution()
    print(solution.minTimeToVisitAllPoints2(points))




