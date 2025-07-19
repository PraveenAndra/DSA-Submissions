class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rooms = []
        count = 0
        for start,end in intervals:
            while rooms !=[] and rooms[0] <= start:
                heapq.heappop(rooms)
            heapq.heappush(rooms,end)
            count = max(count,len(rooms))
        return count
        