class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        dir = [(0,1),(1,0),(0,-1),(-1,0)]
        # res = set()
        r,c = len(board),len(board[0])
        # def search(board,word,i,j,ind,visited):
        #     if ind == len(word):
        #         res.add(word)
        #         return True
        #     for x,y in dir:
        #         nx,ny = x+i,y+j
        #         if 0<=nx<r and 0<=ny<c and (nx,ny) not in visited and board[nx][ny] == word[ind]:
        #             visited.add((nx,ny))
        #             if search(board,word,nx,ny,ind+1,visited):
        #                 return True
        #             visited.remove((nx,ny))
        # start = defaultdict(list)
        # for i in range(r):
        #     for j in range(c):
        #         start[board[i][j]].append((i,j))
        # for word in words:
        #     for i,j in start[word[0]]:
        #         search(board,word,i,j,1,{(i,j)})
        # return list(res)

        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter,{})
            node["$"] = word
        print(trie)
        res = []
        def backtrack(board,x,y,parent):
            letter = board[x][y]
            curr = parent[letter]
            if "$" in curr:
                res.append(curr["$"])
                curr.pop("$")
            for i,j in dir:
                nx,ny = x+i,y+j
                if 0<=nx<r and 0<=ny<c and board[nx][ny] in curr:
                    board[x][y] = "#"
                    backtrack(board,nx,ny,curr)
                    board[x][y] = letter
            if not curr:
                parent.pop(letter)
        for i in range(r):
            for j in range(c):
                if board[i][j] in trie:
                    backtrack(board,i,j,trie)

        return res