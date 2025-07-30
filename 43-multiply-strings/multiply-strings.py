class Solution:
    def multiply(self, nums1: str, nums2: str) -> str:
        if nums1 == "0" or nums2 == "0":
            return "0"
        
        l1,l2 = len(nums1),len(nums2)
        res = [0]*(l1+l2)
        for i in range(l1-1,-1,-1):
            for j in range(l2-1,-1,-1):
                pos1 = i+j+1
                pos2 = i+j
                mul = (ord(nums1[i]) - ord('0'))*(ord(nums2[j]) - ord('0')) + res[pos1]
                res[pos1] = mul % 10
                res[pos2] += mul // 10
        i = 0
        result = ''.join(map(str,res))
        return result.lstrip('0')