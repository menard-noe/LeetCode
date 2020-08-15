from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dico1 = dict()
        dico2 = dict()
        list = []

        for num in nums1:
            dico1[num] = dico1.get(num, 0) + 1
        for num in nums2:
            dico2[num] = dico2.get(num, 0) + 1

        for key in dico1:
            if key in dico2 and dico2[key] > 0 and dico1[key] > 0:
                for i in range(0, min(dico2[key], dico1[key])):
                    list.append(key)
        return list


if __name__ == "__main__":
    # execute only if run as a script
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    solution = Solution()
    print(solution.intersect(nums1, nums2))




