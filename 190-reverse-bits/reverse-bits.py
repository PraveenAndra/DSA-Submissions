class Solution:
    def reverseBits(self, n: int) -> int:
        left = 31 
        res = 0
        while n:
            res += (n&1) << left
            n = n >> 1
            left -= 1
        

        return res
        