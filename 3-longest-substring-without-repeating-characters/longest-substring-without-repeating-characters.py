class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        lastInd = defaultdict(int)
        res = 1
        left = 0
        for i in range(len(s)):
            if s[i] in lastInd:
                left = max(left,lastInd[s[i]]+1)
            lastInd[s[i]] = i
            res = max(res,i-left +1)
        
        return res

        