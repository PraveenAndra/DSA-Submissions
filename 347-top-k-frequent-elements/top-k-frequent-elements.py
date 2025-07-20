class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        heap = []
        for num,i in freq.items():
            heapq.heappush(heap,(i,num))
            if len(heap)> k:
                heapq.heappop(heap)
        return [j for i,j in heap]