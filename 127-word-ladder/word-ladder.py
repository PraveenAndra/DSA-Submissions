class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        patterns = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                patterns[word[:i]+"*"+word[i+1:]].append(word)
        
        beginQ = deque([beginWord])
        endQ = deque([endWord])
        visited_begin,visited_end = {beginWord:1},{endWord:1}
        # print(patterns)
        while beginQ and endQ:
            if len(beginQ) > len(endQ):
                beginQ,endQ = endQ,beginQ
                visited_begin,visited_end = visited_end,visited_begin
            # print(visited_begin,visited_end)
            for q in range(len(beginQ)):
                currWord = beginQ.popleft()
                for i in range(len(currWord)):
                    for word in patterns[currWord[:i]+"*"+currWord[i+1:]]:
                        if word in visited_end:
                            return visited_begin[currWord]+visited_end[word]
                        if word not in visited_begin:
                            visited_begin[word] = visited_begin[currWord]+1
                            beginQ.append(word)
        return 0

        