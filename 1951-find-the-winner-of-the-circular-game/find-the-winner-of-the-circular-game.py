class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # circle = [i for i in range(1,n+1)]
        # start_index = 0
        # while len(circle) > 1:
        #     removal_index = (start_index + k - 1) % len(circle)
        #     circle.pop(removal_index)
        #     start_index = removal_index
        # return circle[0]

        # circle = deque([i for i in range(1,n+1)])
        # while len(circle) > 1:
        #     for i in range(k-1):
        #         circle.append(circle.popleft())
        #     circle.popleft()
        # return circle[0]

        # def findWinner(n,k):
        #     if n == 1:
        #         return 0
        #     return (findWinner(n-1,k)+k)%n 
        # return findWinner(n,k) + 1

        # ans = 0
        # for i in range(2,n+1):
        #     ans = (ans+k)%i
        # return ans+1

        arr = [i for i in range(1,n+1)]
        i = 0
        while len(arr) > 1:
            ind = (i+k-1) % len(arr)
            # print(ind,arr)
            arr.pop(ind)
            i = ind
        return arr[0]















