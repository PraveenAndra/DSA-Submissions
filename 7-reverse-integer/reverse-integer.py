class Solution:
    def reverse(self, x: int) -> int:
        sign = False
        if x < 0:
            sign = True
        x = abs(x)
        curr = 0
        while x > 0:
            rem = x%10
            curr = curr * 10 + rem
            x = x//10
        curr = -curr if sign else curr
        if not -2**31 <= curr <= 2**31-1:
            return 0
        return curr
            
        