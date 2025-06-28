class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        for i in range(1,len(arr)):
            arr[i] += arr[i-1]
        res = 1 if arr[k-1]//k >= threshold else 0
        if len(arr) == k:
            return res
        for i in range(len(arr)-k):
            if (arr[i+k] - arr[i])/k >= threshold:
                res += 1
        return res