class Solution:
    def myPow(self, x: float, n: int) -> float:
        sign = False
        if n < 0:
            sign = True
        res = 1
        n = abs(n)
        while n> 0:
            if n%2==1:
                res *= x
                n-=1
            x*=x
            n//=2
        return res if not sign else (1/res)

        