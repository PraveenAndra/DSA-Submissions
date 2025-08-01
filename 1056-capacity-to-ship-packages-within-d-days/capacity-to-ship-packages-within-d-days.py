class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        s = sum(weights)
        low = max(weights)
        high = s
        res = s
        while low <= high:
            mid = (low+high)//2
            total = 0
            day = 1
            for w in weights:
                if total + w > mid:
                    day += 1
                    total = 0
                total += w
            if day <= days:
                res = mid
                high = mid-1
            else:
                low = mid+1
        return res


        