class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Lookup = {")" : "(" ,"}" : "{" , "]" : "["}  
        for par in s:
            if par in Lookup.values():
                stack.append(par)
            elif stack and Lookup [par] == stack[-1]:
                stack.pop ()
            else:
                return False
        return stack ==[]
