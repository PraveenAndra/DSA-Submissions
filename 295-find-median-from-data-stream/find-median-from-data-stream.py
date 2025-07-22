class MedianFinder:

    def __init__(self):
        self.min = []
        self.max = []
        

    def addNum(self, num: int) -> None:
        if self.max and self.max[0] < num:
            heapq.heappush(self.max,num)
        else:
            heapq.heappush(self.min,-num)
        if len(self.max)+2 <= len(self.min):
            n = heapq.heappop(self.min)
            heapq.heappush(self.max,-n)
        elif len(self.min)+2 <= len(self.max):
            n = heapq.heappop(self.max)
            heapq.heappush(self.min,-n)




        

    def findMedian(self) -> float:
        # print(self.min,self.max)
        if len(self.min) == len(self.max):
            return (self.max[0]-self.min[0])/2
        if len(self.min) > len(self.max):
            return -self.min[0]
        if len(self.max) > len(self.min):
            return self.max[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()