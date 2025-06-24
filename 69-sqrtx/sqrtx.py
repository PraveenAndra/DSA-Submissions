class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        low = 2
        high = x//2
        while low <= high:
            mid = low+(high - low)//2
            val = mid**2
            # print(val)
            if val > x:
                high = mid - 1
            elif val < x:
                low = mid + 1
            else:
                return mid
        return high
        # for i in range(0,x//2+2):
        #     if i**2 == x:
        #         return i
        #     if i**2 > x:
        #         return i-1
        
        