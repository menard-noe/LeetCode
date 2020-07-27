

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if self.is_opening_bracket(char):
                stack.append(char)
            else:
                if len(stack) is 0:
                    return False
                elif self.same_brackets(stack.pop(), char) is False:
                    return False

        if len(stack) is 0:
            return True
        else:
            return False


    '''
    functions could be replaced by using : 
    bracket_map = {"(": ")", "[": "]",  "{": "}"}
    open_par = set(["(", "[", "{"])
    '''

    def is_opening_bracket(self, char: chr):
        if char is '(' or char is '[' or char is '{':
        #if char is '(' or '[' or '{':
            return True
        else:
            return False

    def same_brackets(self, char: chr, char2: chr):
        if char is '(' and char2 is ')':
            return True
        elif char is '[' and char2 is ']':
            return True
        elif char is '{' and char2 is '}':
            return True
        else :
            return False

if __name__ == "__main__":
    # execute only if run as a script
    Input = "{[]}"
    solution = Solution()
    print(solution.isValid(Input))
