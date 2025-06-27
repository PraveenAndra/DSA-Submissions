class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # O(nlogn), O(n)
        # orders = []
        # for trip in trips:
        #     orders.append((trip[1],trip[0]))
        #     orders.append((trip[2],-trip[0]))
        # orders.sort()
        # curr = 0
        # for i,j in orders:
        #     curr += j
        #     if curr > capacity:
        #         return False
        # return True
        #O(n),O(l)
        timestamp = [0]*1001
        for trip in trips:
            timestamp[trip[1]] += trip[0]
            timestamp[trip[2]] -= trip[0]
        change = 0
        for i in timestamp:
            change += i
            if change > capacity:
                return False
        return True