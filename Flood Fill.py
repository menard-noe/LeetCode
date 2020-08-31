from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.dico = dict()
        sr_max = len(image)
        sc_max = len(image[0])

        def utils(image: List[List[int]], sr: int, sc: int, newColor: int, startingColor: int)-> List[List[int]]:
            self.dico[sr, sc] = 1
            if image[sr][sc] == startingColor:
                image[sr][sc] = newColor
                if sr + 1 < sr_max and (sr + 1, sc) not in self.dico:
                    utils(image, sr + 1, sc, newColor, startingColor)
                if sr - 1 >= 0 and (sr - 1, sc) not in self.dico:
                    utils(image, sr - 1, sc, newColor, startingColor)
                if sc + 1 < sc_max and (sr, sc + 1) not in self.dico:
                    utils(image, sr, sc + 1, newColor, startingColor)
                if sc - 1 >= 0 and (sr, sc - 1) not in self.dico:
                    utils(image, sr, sc - 1, newColor, startingColor)
            return image

        utils(image, sr, sc, newColor, image[sr][sc])
        return image


if __name__ == "__main__":
    # execute only if run as a script
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2
    solution = Solution()
    print(solution.floodFill(image, sr, sc, newColor))
