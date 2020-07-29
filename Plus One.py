from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i, e in reversed(list(enumerate(digits))):
            print(i, e)
            if e < 9:
                digits[i] += 1
                return digits

            else:
                if i == 0:
                    digits[i] = 0
                    digits.insert(0, 1)
                    return digits
                else:
                    digits[i] = 0
                    continue


if __name__ == "__main__":
    # execute only if run as a script
    nums = [9,0]
    target = 0
    solution = Solution()
    print(solution.plusOne(nums))


