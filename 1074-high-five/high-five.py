class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = defaultdict(list)
        for item in items:
            id,score = item
            if len(scores[id]) == 5 and scores[id][0] < score:
                heapq.heappop(scores[id])
            if len(scores[id]) < 5:
                heapq.heappush(scores[id],score)
        
        res = []
        for id in sorted(scores):
            res.append([id,sum(scores[id])//5])
        return res
        