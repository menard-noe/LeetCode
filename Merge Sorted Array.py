import math
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        index_array_1 = m - 1
        index_array_2 = n - 1
        index_final_array = len(nums1) - 1

        while index_array_2 >= 0:
            if index_array_1 >= 0 and nums1[index_array_1] > nums2[index_array_2]:
                nums1[index_final_array] = nums1[index_array_1]
                index_array_1 -= 1
            else:
                nums1[index_final_array] = nums2[index_array_2]
                index_array_2 -= 1
            index_final_array -= 1


if __name__ == "__main__":
    # execute only if run as a script
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solution = Solution()
    print(solution.merge(nums1, m, nums2, n))