class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1,l2 = len(text1),len(text2)
        dp = [[0]*(l2+1) for i in range(l1+1)]
        prev= [0]*(l2+1)
        curr = [0]*(l2+1)
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if text1[i-1] == text2[j-1]:
                    curr[j] = prev[j-1]+1
                else:
                    curr[j] = max(prev[j],curr[j-1])
            prev,curr = curr,prev 
        return prev[-1]

        