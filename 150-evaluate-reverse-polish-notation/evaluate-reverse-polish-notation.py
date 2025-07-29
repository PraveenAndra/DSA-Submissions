class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ["*","+","-","/"]:
                num2,num1 = stack.pop(),stack.pop()
                if i=="*":
                    stack.append(num1*num2)
                elif i=="/":
                    stack.append(int(num1/num2))
                elif i =="+":
                    stack.append(num1+num2)
                else:
                    stack.append(num1-num2)
            else:
                stack.append(int(i))
        return stack.pop()
        