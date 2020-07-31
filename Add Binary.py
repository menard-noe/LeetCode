import math


class Solution:
    def addBinary(self, a: str, b: str) -> str:

        c = ""
        carry = 0

        while a and b:
            last_digit_a = a[-1:]
            last_digit_b = b[-1:]

            a = a[:-1]
            b = b[:-1]

            addition = int(last_digit_a) + int(last_digit_b) + carry
            carry = math.floor(addition / 2)
            last_digit_c = addition % 2
            c = str(last_digit_c) + c

        if a:
            while a:
                last_digit_a = a[-1:]
                a = a[:-1]
                addition = int(last_digit_a) + carry
                carry = math.floor(addition / 2)
                last_digit_c = addition % 2
                c = str(last_digit_c) + c
        elif b:
            while b:
                last_digit_b = b[-1:]
                b = b[:-1]
                addition = int(last_digit_b) + carry
                carry = math.floor(addition / 2)
                last_digit_c = addition % 2
                c = str(last_digit_c) + c
        if carry == 1:
            c = "1" + c
        return c


if __name__ == "__main__":
    # execute only if run as a script
    a = "1111"
    b = "10"
    solution = Solution()
    print(solution.addBinary(a, b))