class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        start,end = float('-inf'),float('-inf')
        # print(intervals)
        for i,j in intervals:
            if i < end :
                res += 1
                end = min(end,j)
            else:
                start,end = i,j
        return res

        