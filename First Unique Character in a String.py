class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0:
            return -1
        dico = dict()

        for i, char in enumerate(s):
            if char in dico:
                dico[char] = 999999
            else:
                dico[char] = i

        index = 999999
        for key in dico:
            if dico[key] < index:
                index = dico[key]
        if index == 999999:
            index = -1
        return index



if __name__ == "__main__":
    # execute only if run as a script
    input = "loveleetcode"
    solution = Solution()
    print(solution.firstUniqChar(input))
