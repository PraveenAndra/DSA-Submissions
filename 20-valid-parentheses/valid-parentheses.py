class Solution:
    def isValid(self, s: str) -> bool:
        new_dict= {"(":")","{":"}","[":"]"}
        stack = []
        if len(s)%2!=0:
            return False
        for i in s:
            if i in new_dict.keys():
                stack.append(new_dict[i])
            elif (len(stack)==0 or stack.pop()!=i):
                return False
        if len(stack)!=0: return False
        return True
            
            