class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # intervals.sort()
        # heap = []
        # for i,j in intervals:
        #     heapq.heappush(heap,(j-i+1,i,j))
        # res = []
        # for i in range(len(queries)):
        #     temp = []
        #     while heap:
        #         diff,start,end = heapq.heappop(heap)
        #         temp.append((diff,start,end))
        #         if start <= queries[i] <=end:
        #             res.append(diff)
        #             break
        #     for j in temp:
        #         heapq.heappush(heap,j)
        #     if len(res)!= i+1:
        #         res.append(-1)
        # return res
        ans = [-1]*len(queries)

        intervals.sort()
        qidxs = list(range(len(queries)))
        qidxs.sort(key=lambda i: queries[i])
        print(qidxs)

        k = 0 # next interval index to push
        ivals = [] # (size, start, end) for all intervals containing next query, min heap by size
        for i in qidxs:
            q = queries[i]

            while ivals and ivals[0][2] < q: heappop(ivals)
            
            while k < len(intervals) and intervals[k][0] <= q:
                if intervals[k][1] >= q:
                    # skip intervals that start later, but have already ended
                    # (we'd pop them to maintain RI anyway)
                    heappush(ivals, (intervals[k][1]-intervals[k][0]+1, intervals[k][0], intervals[k][1]))
                k += 1

            if ivals:
                ans[i] = ivals[0][0]

        return ans


        