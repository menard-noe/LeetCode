from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        min_val = float("inf")
        max_val = - float("inf")
        count = 0
        sum = 0

        for val in salary:
            min_val = min(min_val, val)
            max_val = max(max_val, val)
            count += 1
            sum += val

        return (sum - min_val - max_val)/(count - 2)


if __name__ == "__main__":
    salary = [4000,3000,1000,2000]
    solution = Solution()
    print(solution.average(salary))