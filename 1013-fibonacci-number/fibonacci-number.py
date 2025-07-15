class Solution:
    def fib(self, n: int) -> int:
        first = 0
        prev = 1
        if n <=1:
            return n
        curr = 1

        for i in range(2,n+1):
            curr = first+prev
            first = prev
            prev = curr
        return prev
            


        