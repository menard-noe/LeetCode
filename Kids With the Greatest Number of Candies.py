from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = - float("inf")
        for candy in candies:
            max_candy = max(max_candy, candy)

        res = []
        for candy in candies:
            if candy + extraCandies >= max_candy:
                res.append(True)
            else:
                res.append(False)

        return res


if __name__ == "__main__":
    candies = [12,1,12]
    extraCandies = 10
    solution = Solution()
    print(solution.kidsWithCandies(candies, extraCandies))