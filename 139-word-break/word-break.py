class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dfs(ind):
            if ind == len(s):
                return True
            if ind >= len(s):
                return False
            for i in range(ind+1,len(s)+1):
                if s[ind:i] in wordDict and dfs(i):
                    return True
            return False
        return dfs(0)
        