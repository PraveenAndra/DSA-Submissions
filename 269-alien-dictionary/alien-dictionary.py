class Solution:
    def alienOrder(self, words: List[str]) -> str:
        edges = defaultdict(set)
        indegree = defaultdict(int)
        for word in words:
            for c in word:
                indegree[c] = 0
        for first_word, second_word in zip(words, words[1:]):
            print(first_word,second_word)
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in edges[c]:
                        edges[c].add(d)
                        indegree[d] += 1
                    break
            else:
                if len(second_word) < len(first_word):
                    return ""
        
        q = deque()
        for i in indegree:
            if indegree[i] == 0:
                q.append(i)
        print(edges,indegree,q)
        res = []
        while q:
            char = q.popleft()
            res.append(char)
            for i in edges[char]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        if len(res) < len(indegree):
            return ""
        return "".join(res)
