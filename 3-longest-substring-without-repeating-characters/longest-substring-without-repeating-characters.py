class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indexes = defaultdict(int)
        left = 0
        res = 0
        for right in range(len(s)):
            if s[right] in indexes:
                left = max(indexes[s[right]] + 1,left)
            indexes[s[right]] = right
            res = max(res,right-left+1)
        return res


        