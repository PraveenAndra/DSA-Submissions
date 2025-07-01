class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        curr_rooms = []
        intervals.sort()
        min_num = 0
        for i,j in intervals:
            if curr_rooms:
                if curr_rooms[0] <= i:
                    heapq.heappop(curr_rooms)
            heapq.heappush(curr_rooms,j)
            min_num = max(min_num,len(curr_rooms))
        return min_num
        