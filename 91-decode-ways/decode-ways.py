class Solution:
    def numDecodings(self, s: str) -> int:
        # dp = [0 for i in range(len(s)+1)]
        # dp[0] = 1
        # dp[1] = 0 if s[0]=="0" else 1
        # for i in range(2,len(dp)):
        #     if dp[i-1]!=0:
        #         dp[i] = dp[i-1]
        #     two_digit = int(s[i-2:i])
        #     if two_digit >= 10 and two_digit <=26:
        #         dp[i] += dp[i-2]
        # return dp[-1]


    
        # def backtrack(i,s):
        #     if len(s) == i:
        #         return 1
        #     if s[i] == "0":
        #         return 0
        #     if i == len(s) - 1:
        #         return 1
        #     answer = backtrack(i+1,s)
        #     if int(s[i:i+2]) <= 26:
        #         answer += backtrack(i+2,s)
        #     # one letter
        #     return answer
        # return backtrack(0,s)
        
        # if s[0] == "0":
        #     return 0
        # dp = [0]* (len(s)+1)
        # dp[1] = 1
        # dp[0] = 1
        # for i in range(1,len(s)):
        #     if s[i] != "0":
        #         dp[i+1] = dp[i]
        #     if int(s[i-1:i+1])>=10 and int(s[i-1:i+1]) <= 26:
        #         dp[i+1] += dp[i-1]
        # # print(dp)
        # return dp[-1]
        one_back = 1 if s[0]!="0" else 0
        two_back = 1
        for i in range(1,len(s)):
            curr = 0
            if s[i] != "0":
                curr = one_back
            two_digit = int(s[i-1:i+1])
            if two_digit >= 10 and two_digit <=26:
                curr += two_back
            two_back = one_back
            one_back = curr
        return one_back
            
















