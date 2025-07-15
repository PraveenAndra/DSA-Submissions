class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def canPlace(x,m):
            last_placed = 0
            m -= 1
            for i in range(1,len(position)):
                if position[i] - position[last_placed] >= x:
                    m -= 1
                    last_placed = i
            return m <= 0

        position.sort()
        left = 1
        right = position[-1]
        res = 1
        while left <= right:
            mid = left + (right-left)//2
            if canPlace(mid,m):
                res = max(res,mid)
                left = mid+1
            else:
                right = mid-1
        return res

