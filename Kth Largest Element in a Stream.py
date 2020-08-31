from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        left = 0
        right = len(self.nums)

        while left < right:
            middle = (left + right) // 2
            if self.nums[middle] < val:
                left = middle + 1
            else:
                right = middle

        self.nums.insert(left, val)
        return self.nums[-self.k]




# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)




if __name__ == "__main__":
    # execute only if run as a script
    k = 3
    arr = [4, 5, 8, 2]
    kthLargest = KthLargest(3, arr)
    print(kthLargest.add(3))
    print(kthLargest.add(5))
    print(kthLargest.add(10))
    print(kthLargest.add(9))
    print(kthLargest.add(4))