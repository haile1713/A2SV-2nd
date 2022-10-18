class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack_list = []
        for A in tokens:
            if A == "+":
                stack_list.append(stack_list.pop() + stack_list.pop())
            elif A == "-":
                x,y = stack_list.pop(),stack_list.pop()
                stack_list.append (y-x)
            elif A == "*":
                stack_list.append(stack_list.pop() * stack_list.pop())
            elif A == "/":
                x,y = stack_list.pop(),stack_list.pop()
                stack_list.append (int(y/x))
            else:
                stack_list.append (int(A))
        return stack_list [0]
        
