class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0

        for char in moves:
            if char == 'U':
                y += 1
            if char == 'D':
                y -= 1
            if char == 'L':
                x -= 1
            if char == 'R':
                x += 1
        return x == 0 and y == 0


if __name__ == "__main__":
    # execute only if run as a script
    input = "UD"
    solution = Solution()
    print(solution.judgeCircle(input))