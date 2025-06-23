class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for i in range(numCourses)]
        inorder = [0]*numCourses
        for i,j in prerequisites:
            adj_list[j].append(i)
            inorder[i] += 1
        stack = deque()
        for i in range(numCourses):
            if inorder[i] == 0:
                stack.append(i)
        res = 0
        visited = [False]*numCourses
        order = []
        while stack:
            curr = stack.popleft()
            if visited[curr]:
                continue
            res += 1
            order.append(curr)
            visited[curr] = True
            for i in adj_list[curr]:
                inorder[i] -= 1
                if inorder[i] == 0:
                    stack.append(i)
        return order if res==numCourses else []
