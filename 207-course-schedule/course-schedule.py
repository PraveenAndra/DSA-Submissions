class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_list = [[] for i in range(numCourses)]
        


        # # DFS Solution
        # for i,j in prerequisites:
        #     adj_list[i].append(j)
        # def dfs(curr,visited,stack):
        #     if stack[curr]:
        #         return True
        #     if visited[curr]:
        #         return False
        #     visited[curr] = True
        #     stack[curr] = True
        #     for i in adj_list[curr]:
        #         if dfs(i,visited,stack):
        #             return True
        #     stack[curr] = False
        #     return False
        
        # visited = [False for i in range(numCourses)]
        # stack = [False for i in range(numCourses)]

        # for i in range(numCourses):
        #     if dfs(i,visited,stack):
        #         return False
        # return True

        #Topological Sort
        inorder = [0]*numCourses
        for i,j in prerequisites:
            adj_list[i].append(j)
            inorder[j] += 1
        stack = deque()
        for i in range(numCourses):
            if inorder[i] == 0:
                stack.append(i)
        res = 0
        visited = [False]*numCourses
        while stack:
            curr = stack.popleft()
            if visited[curr]:
                continue
            res += 1
            visited[curr] = True
            for i in adj_list[curr]:
                inorder[i] -= 1
                if inorder[i] == 0:
                    stack.append(i)
        return res == numCourses




        