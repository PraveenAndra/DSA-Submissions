class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i,point in enumerate(points):
            x,y = point[0], point[1]
            d = (x**2+y**2)**0.5
            heapq.heappush(heap,(d,i))
        res = []
        for i in range(k):
            d,i = heapq.heappop(heap)
            res.append(points[i])
        return res



        