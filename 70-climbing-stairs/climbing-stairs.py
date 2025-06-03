class Solution:
    def climbStairs(self, n: int) -> int:

        prev = 0
        curr = 1

        for i in range(1, n+1):
            temp = curr + prev
            prev = curr
            curr = temp
        return curr
        