class Solution:
    def findLucky(self, arr: List[int]) -> int:
        l = Counter(arr)
        res = -1
        for i in set(arr):
            if l[i] == i:
                res = max(res,i)
        return res
        