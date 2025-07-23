class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        for start,end in intervals:
            while res and res[-1][1] >= start:
                prev_s,prev_end = res[-1]
                res.pop()
                start = min(prev_s,start)
                end = max(prev_end,end)
            res.append((start,end))
        return res
