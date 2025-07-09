class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        conf = []
        intervals.sort()
        res = 0
        for start,end in intervals:
            while conf and conf[0] <= start:
                heapq.heappop(conf)
            heapq.heappush(conf,end)  
            res = max(res,len(conf))
        return res

        