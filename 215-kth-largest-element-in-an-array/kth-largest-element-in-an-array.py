class Solution:
    def findKthLargest(self, nums, k):
        # arr = []
        # for i in nums:
        #     if len(arr) == k and i > arr[0]:
        #         heapq.heappop(arr)
        #         heapq.heappush(arr,i)
        #     elif len(arr) < k:
        #         heapq.heappush(arr,i)
        # return arr[0]

        def quick_select(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []

            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)
            
            if k <= len(left):
                return quick_select(left, k)
            
            if len(left) + len(mid) < k:
                return quick_select(right, k - len(left) - len(mid))
            
            return pivot
        
        return quick_select(nums, k)

                