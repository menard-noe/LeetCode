from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people

        index = 0
        while candies != 0:
            if (index + 1) <= candies:
                res[index % num_people] += (index + 1)
                candies -= index + 1
            else:
                res[index % num_people] += candies
                candies = 0
            index += 1
        return res


if __name__ == "__main__":
    # execute only if run as a script
    candies = 10
    num_people = 3
    solution = Solution()
    print(solution.distributeCandies(candies, num_people))