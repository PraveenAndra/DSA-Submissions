class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {")":"(","}":"{","]":"["}
        for i in s:
            if i in match:
                if stack and stack[-1] != match[i]:
                    return False
                if not stack:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return True if not stack else False

                


        