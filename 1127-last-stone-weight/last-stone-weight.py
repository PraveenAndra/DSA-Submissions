class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapify(stones)
        while stones:
            if len(stones) == 1:
                return -stones[0]
            y,x = heapq.heappop(stones),heapq.heappop(stones)
            # print(y,x)
            if x == y:
                continue
            if x!=y:
                heapq.heappush(stones,y-x)

        return 0
        