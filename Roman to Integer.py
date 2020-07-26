class Solution:
    def romanToInt(self, s: str) -> int:

        dico = dict({})
        dico['I'] = 1
        dico['V'] = 5
        dico['X'] = 10
        dico['L'] = 50
        dico['C'] = 100
        dico['D'] = 500
        dico['M'] = 1000

        result = 0
        temp_addition = 0

        for char in s:
            if dico[char] > temp_addition != 0:
                result += dico[char] - temp_addition
                temp_addition = 0
            else:
                result += temp_addition
                temp_addition = dico[char]

        result += temp_addition
        return result


if __name__ == "__main__":
    # execute only if run as a script
    Input = "MCMXCIV"
    solution = Solution()
    print(solution.romanToInt(Input))