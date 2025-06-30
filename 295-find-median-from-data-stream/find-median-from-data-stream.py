class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        # if self.large and num > self.large[0]:
        #     heapq.heappush(self.large,num)
        # else:
        #     heapq.heappush(self.small, -num)
        # if len(self.small) > len(self.large)+1:
        #     s = heapq.heappop(self.small)
        #     heapq.heappush(self.large,-s)
        # if len(self.large) > len(self.small)+1:
        #     s = heapq.heappop(self.large)
        #     heapq.heappush(self.small,-s)
        if len(self.small) == len(self.large):
            heapq.heappush(self.large,num)
            heapq.heappush(self.small,-heapq.heappop(self.large))
        else:
            heapq.heappush(self.small,-num)
            heapq.heappush(self.large,-heapq.heappop(self.small))

    def findMedian(self) -> float:
        # if len(self.small) > len(self.large):
        #     return -self.small[0]
        # elif len(self.large) > len(self.small):
        #     return self.large[0]
        # else:
        #     return ((-self.small[0]+self.large[0])/2)
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0])/2
        else:
            return -self.small[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()