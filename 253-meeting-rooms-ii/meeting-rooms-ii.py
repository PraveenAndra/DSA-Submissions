class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        available = 0
        start = []
        for i,j in intervals:
            start.append((i,1))
            start.append((j,-1))
        start.sort()
        curr = 0
        for i,j in start:
            curr += j
            available = max(available,curr)
        return available
        



        