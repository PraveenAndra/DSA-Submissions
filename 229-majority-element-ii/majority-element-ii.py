class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1,cand2 = None,None
        c1,c2 = 0,0
        for num in nums:
            if c1 == 0 and num!=cand2:
                cand1 = num
                c1 += 1
            elif c2 == 0 and num!= cand1:
                cand2 = num
                c2+=1
            elif num == cand1:
                c1 += 1
            elif num == cand2:
                c2 += 1
            else:
                c1 -=1
                c2 -=1
        print(cand1,cand2)
        res = []
        c1,c2 = 0,0
        for num in nums:
            if num == cand1:
                c1+=1
            elif num == cand2:
                c2 +=1
        n = len(nums)
        if c1 > n//3:
            res.append(cand1)
        if c2>n//3:
            res.append(cand2)
        return res
            