import math


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        cow = 0

        s_dico = dict()
        g_dico = dict()

        for i in range (0, len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                if secret[i] in s_dico:
                    s_dico[secret[i]] += 1
                else:
                    s_dico[secret[i]] = 1
                if guess[i] in g_dico:
                    g_dico[guess[i]] += 1
                else:
                    g_dico[guess[i]] = 1
        for key in s_dico:
            if key in g_dico:
                cow += min(s_dico[key], g_dico[key])

        return str(bull) + "A" + str(cow) + "B"


if __name__ == "__main__":
    # execute only if run as a script
    secret = "1123"
    guess = "0111"
    solution = Solution()
    print(solution.getHint(secret, guess))