class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # visited = set()
        adj_list = defaultdict(list)
        indegree = [0]*numCourses
        for i,j in prerequisites:
            adj_list[j].append(i)
            indegree[i] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        order = []
        while q:
            course = q.popleft()
            for i in adj_list[course]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
            order.append(course)
        return len(order) == numCourses
            

        
        # order = []
        # def dfs(curr,visited,inStack):
        #     if inStack[curr]:
        #         return True
        #     if curr in visited:
        #         return False
        #     inStack[curr] = True
        #     for n in adj_list[curr]:
        #         if dfs(n,visited,inStack):
        #             return True
        #     visited.add(curr)
        #     order.append(curr)
        #     inStack[curr] = False
        #     return False
        # inStack = [False]*numCourses
        # # for i in range(numCourses):
        # #     if dfs(i,visited,inStack):
        # #         return False
        # dfs(1,visited,inStack)
        # print(order)
        # return True
        