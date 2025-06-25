class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        print(intervals)
        n = 0
        i= 1
        while i < len(intervals):
            if intervals[i][0] < intervals[i-1][1]:
                n += 1
                intervals.pop(i)
            else:
                i += 1
        return n
        