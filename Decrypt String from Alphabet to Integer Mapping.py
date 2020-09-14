import heapq
from typing import List


class Solution:
    def freqAlphabets(self, s: str) -> str:
        heap = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                heap.append(chr(int(s[i-2:i]) + 96))
                i = i - 3
            else:
                heap.append(chr(int(s[i]) + 96))
                i = i - 1
        heap.reverse()
        res = ''.join(val for val in heap)
        return res


if __name__ == "__main__":
    # execute only if run as a script
    s = "10#11#12"
    solution = Solution()
    print(solution.freqAlphabets(s))
