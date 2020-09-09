from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        sum = 0
        cum_sum = []

        for num in A:
            sum += num
            cum_sum.append(sum)

        if sum % 3 != 0:
            return False

        third = sum / 3

        left = 0
        right = len(cum_sum) - 2

        while left < right:
            if cum_sum[left] == third and cum_sum[right] == third * 2:
                return True
            elif cum_sum[left] == third:
                right -= 1
            elif cum_sum[right] == third * 2:
                left += 1
            else:
                right -= 1
                left += 1
        return False


if __name__ == "__main__":
    # execute only if run as a script
    input = [1,-1,1,-1]
    solution = Solution()
    print(solution.canThreePartsEqualSum(input))