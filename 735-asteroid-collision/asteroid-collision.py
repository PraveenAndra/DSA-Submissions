class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            flag = True
            while stack and stack[-1] > 0 and i < 0:
                if abs(stack[-1]) == abs(i):
                    stack.pop()
                    flag = False
                    break
                elif abs(stack[-1]) < abs(i):
                    stack.pop()
                else:
                    flag = False
                    break
            if flag:
                stack.append(i)
            
        return stack
                  

        


        