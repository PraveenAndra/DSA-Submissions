class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        prev_end = points[0][1]
        res = 1
        for start,end in points[1:]:
            if start > prev_end:
                res+= 1
                prev_end = end
        return res



        