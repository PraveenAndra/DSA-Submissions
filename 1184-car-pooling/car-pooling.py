class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        orders = []
        for trip in trips:
            orders.append([trip[1],trip[0]])
            orders.append([trip[2],-trip[0]])
        orders.sort()
        curr = 0
        for order in orders:
            curr += order[1]
            if curr > capacity:
                return False
        return True

            

            


        