class Solution:
    def findKthLargest(self, nums, k):
        arr = []
        for i in nums:
            if len(arr) == k and i > arr[0]:
                heapq.heappop(arr)
                heapq.heappush(arr,i)
            elif len(arr) < k:
                heapq.heappush(arr,i)
        return arr[0]

                