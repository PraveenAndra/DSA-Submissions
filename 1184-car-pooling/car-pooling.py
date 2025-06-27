class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # orders = []
        # for trip in trips:
        #     orders.append([trip[1],trip[0]])
        #     orders.append([trip[2],-trip[0]])
        # orders.sort()
        # curr = 0
        # for order in orders:
        #     curr += order[1]
        #     if curr > capacity:
        #         return False
        # return True
        # timestamp = [0] * 1001
        # for trip in trips:
        #     timestamp[trip[1]] += trip[0]
        #     timestamp[trip[2]] -= trip[0]

        # used_capacity = 0
        # for passenger_change in timestamp:
        #     used_capacity += passenger_change
        #     if used_capacity > capacity:
        #         return False

        # return True




        # orders = []
        # for cap,fr,to in trips:
        #     orders.append((fr,cap))
        #     orders.append((to,-cap))
        # orders.sort()
        # curr = 0
        # for i in range(len(orders)):
        #     curr += orders[i][1]
        #     if curr > capacity:
        #         return False
        # return True
        points = [0]*1001
        for i in trips:
            points[i[1]] += i[0]
            points[i[2]] -= i[0]
        change = 0
        for i in points:
            if i+change > capacity:
                return False
            change += i
        return True



















            

            


        