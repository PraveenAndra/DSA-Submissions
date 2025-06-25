class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        arr = [0]+arr
        for i in range(1,k):
            arr[i] = arr[i] + arr[i-1]
        for i in range(k,len(arr)):
            arr[i] = arr[i] + arr[i-1]
            if (arr[i] - arr[i-k]) / k >= threshold:
                res += 1
        return res

        # for i in range(len(arr)-k+1):
        #     if sum(arr[i:i+k])/k >= threshold:
        #         res+= 1
        # return res
        