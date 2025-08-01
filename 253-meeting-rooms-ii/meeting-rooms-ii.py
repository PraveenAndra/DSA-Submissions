class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        minRooms = float('-inf')
        rooms = []
        for start,end in intervals:
            while rooms and rooms[0] <= start:
                heapq.heappop(rooms)
            heapq.heappush(rooms,end)
            minRooms = max(minRooms,len(rooms))
        return minRooms if minRooms != float('inf') else 0