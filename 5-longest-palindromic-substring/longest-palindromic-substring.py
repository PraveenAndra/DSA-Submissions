class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp = [[0]*len(s) for i in range(len(s))]
        # res = [None,None]
        # for i in range(len(s)):
        #     dp[i][i] = 1
        #     res = [i,i]
        # for i in range(len(s)-1):
        #     if s[i]==s[i+1]:
        #         dp[i][i+1] = 1
        #         res = [i,i+1]
        # for diff in range(2,len(s)):
        #     for i in range(len(s)-diff):
        #         j = i+diff
        #         if s[i] ==s[j] and dp[i+1][j-1]:
        #             dp[i][j] = 1
        #             res = [i,j]
        # return s[res[0]:res[1]+1]
        def expand(i, j):
            left = i
            right = j

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return right - left - 1

        ans = [0, 0]

        for i in range(len(s)):
            odd_length = expand(i, i)
            if odd_length > ans[1] - ans[0] + 1:
                dist = odd_length // 2
                ans = [i - dist, i + dist]

            even_length = expand(i, i + 1)
            if even_length > ans[1] - ans[0] + 1:
                dist = (even_length // 2) - 1
                ans = [i - dist, i + 1 + dist]

        i, j = ans
        return s[i : j + 1]


        