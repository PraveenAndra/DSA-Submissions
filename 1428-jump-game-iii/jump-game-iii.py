class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = [False]*len(arr)

        q = deque([start])
        while q:
            curr = q.popleft()
            if arr[curr] == 0:
                return True
            left,right = curr - arr[curr], curr+arr[curr]
            if left >=0 and not visited[left]:
                q.append(left)
            if right <len(arr) and not visited[right]:
                q.append(right)
            visited[curr] = True
        return False
             