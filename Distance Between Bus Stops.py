from typing import List

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        clockwise = 0
        counterclockwise = 0
        start_clockwise = start

        while start_clockwise != destination:
            clockwise += distance[start_clockwise]
            start_clockwise += 1
            start_clockwise = start_clockwise % len(distance)

        while start != destination:
            counterclockwise += distance[start - 1]
            start -= 1
            start = start % len(distance)

        return min(clockwise, counterclockwise)


if __name__ == "__main__":
    # execute only if run as a script
    distance = [1, 2, 3, 4]
    start = 0
    destination = 3
    solution = Solution()
    print(solution.distanceBetweenBusStops(distance, start, destination))




