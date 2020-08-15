
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        left = 1
        right = num

        while left != right:
            middle = (left + right) // 2
            left_root = left * left
            right_root = right * right
            middle_root = middle * middle
            if left_root == num or right_root == num:
                return True
            elif middle_root < num:
                left = middle + 1
            else:
                right = middle
        return False



if __name__ == "__main__":
    # execute only if run as a script
    Input = 15
    solution = Solution()
    print(solution.isPerfectSquare(Input))
