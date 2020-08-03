import math


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(nums, left, right):
            if left > right: return
            mid = (left + right) // 2
            curNode = TreeNode(nums[mid])
            curNode.left = helper(nums, left, mid - 1)
            curNode.right = helper(nums, mid + 1, right)
            return curNode

        return helper(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    # execute only if run as a script
    input = [-10,-3,0,5,9]
    solution = Solution()
    res = solution.sortedArrayToBST(input)
    print("")