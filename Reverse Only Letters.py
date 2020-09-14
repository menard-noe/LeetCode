# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        res = []
        j = len(S) - 1

        for char in S:
            if char.isalpha():
                while not S[j].isalpha():
                    j -= 1
                res.append(S[j])
                j -= 1
            else:
                res.append(char)

        return "".join(res)

if __name__ == "__main__":
    # execute only if run as a script
    Input = "ab-cd"
    solution = Solution()
    print(solution.reverseOnlyLetters(Input))