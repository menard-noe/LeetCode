from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        dico = dict()

        last = -999999
        for i, seat in enumerate(seats):
            if seat == 1:
                last = i
                dico[i] = 0
            else:
                dico[i] = i - last

        last = 999999
        for i in range(len(seats) - 1, -1, -1):
            if seats[i] == 1:
                last = i
                dico[i] = 0
            else:
                dico[i] = min(last - i, dico[i])

        max = 0
        for key in dico:
            if dico[key] > max:
                max = dico[key]

        return max


class Solution2(object):
    def maxDistToClosest(self, seats):
        people = (i for i, seat in enumerate(seats) if seat)
        prev, future = None, next(people)

        ans = 0
        for i, seat in enumerate(seats):
            if seat:
                prev = i
            else:
                while future is not None and future < i:
                    future = next(people, None)

                left = float('inf') if prev is None else i - prev
                right = float('inf') if future is None else future - i
                ans = max(ans, min(left, right))

        return ans

if __name__ == "__main__":
    # execute only if run as a script
    nums = [0,1,0,0,0,1,0,1,0]
    solution = Solution()
    print(solution.maxDistToClosest(nums))