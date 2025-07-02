class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # intervals.sort(key = lambda x:x[1])
        # prev_end = intervals[0][1]
        # res = 0
        # for i in intervals[1:]:
        #     if i[0] >= prev_end:
        #         prev_end = i[1]
        #     else:
        #         res += 1
        # return res

        intervals.sort(key=lambda x: x[0])
        
        # Step 2: Initialize variables
        end = intervals[0][1]  # The end of the first interval
        count = 0  # Number of intervals to remove
        
        # Step 3: Iterate through the intervals starting from the second one
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:  # If there's an overlap
                count += 1  # We need to remove this interval
                # We keep the interval with the smallest end time
                end = min(end, intervals[i][1])
            else:
                # No overlap, just update the end to the current interval's end
                end = intervals[i][1]
        
        return count