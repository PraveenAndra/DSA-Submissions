class Solution:
    def mySqrt(self, x: int) -> int:
        # if x<2:
        #     return x
        # low = 2
        # high = x//2
        # while low <= high:
        #     mid = low+(high - low)//2
        #     val = mid**2
        #     # print(val)
        #     if val > x:
        #         high = mid - 1
        #     elif val < x:
        #         low = mid + 1
        #     else:
        #         return mid
        # return high
        # for i in range(0,x//2+2):
        #     if i**2 == x:
        #         return i
        #     if i**2 > x:
        #         return i-1

        # for i in range(0,x//2+2):
        #     if i*i == x:
        #         return i
        #     elif i*i > x:
        #         return i-1
        

        if x < 2:
            return x
        
        low = 1
        high = x
        while low <= high:
            mid = low + (high-low)//2
            if mid*mid == x:
                return mid
            if mid*mid < x:
                low = mid+1
            else:
                high = mid -1
        return high


        
















        
        