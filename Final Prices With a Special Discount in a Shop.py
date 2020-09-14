from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # Use a stack to store elements idxs and res to store our results.
        stack = []
        res = [0] * len(prices)
        for i in range(len(prices)):
            # While we have elements on the stack and top element is >= to the current.
            while stack and (prices[stack[-1]] >= prices[i]):
                # Pop the elements idx from the stack and store the resulted price in our array.
                idx = stack.pop()
                res[idx] = prices[idx] - prices[i]
            stack.append(i)
        # If there are elements left it means there was no smaller element so there is 0 discount.
        while stack:
            i = stack.pop()
            res[i] = prices[i]

        return res
if __name__ == "__main__":
    prices = [8,4,6,2,3]
    solution = Solution()
    print(solution.finalPrices(prices))