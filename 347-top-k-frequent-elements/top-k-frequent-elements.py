class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup = {}
        l = len(nums)
        top_k = [set() for i in range(l+1)]
        for i in nums:
            if i not in lookup:
                lookup[i] = 1
                top_k[1].add(i)
            else:
                curr = lookup[i]
                lookup[i] += 1
                top_k[curr].remove(i)
                top_k[curr+1].add(i)
        res = []
        ind = l
        while k>0:
            if top_k[ind] != set():
                res.extend(top_k[ind])
                k-=len(top_k[ind])
            ind -= 1
        print(top_k)
        return res


            

        