class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        prev_end = intervals[0][1]
        res = 0
        for i in intervals[1:]:
            if i[0] >= prev_end:
                prev_end = i[1]
            else:
                res += 1
        return res