class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        heap = []
        for i,j in counter.items():
            heapq.heappush(heap,(-j,i))
        res = []
        while heap:
            count,c = heapq.heappop(heap)
            if not res or c!=res[-1]:
                res.append(c)
                if count+1 != 0:
                    heapq.heappush(heap,(count+1,c))
            else:
                if not heap: return ""
                count2,c2 = heapq.heappop(heap)
                res.append(c2)
                if count2+1!=0:
                    heapq.heappush(heap,(count2+1,c2))
                heapq.heappush(heap,(count,c))
        return ''.join(res)