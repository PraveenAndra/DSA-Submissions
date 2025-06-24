class Solution:
    def mySqrt(self, x: int) -> int:
        # low = 1
        # high = x
        # while low < high:
        #     mid = (high + low)//2
        #     val = mid**2
        #     print(val)
        #     if val > x:
        #         high = mid
        #     elif val < x:
        #         low = mid
        #     else:
        #         return mid
        # return low
        for i in range(0,x//2+2):
            if i**2 == x:
                return i
            if i**2 > x:
                return i-1
        
        