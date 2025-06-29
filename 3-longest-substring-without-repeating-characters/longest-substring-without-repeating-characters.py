class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = {}
        left = 0
        max_len = 0
        for right in range(len(s)):
            # print(char,left,right)
            if s[right] in char: 
                left = max(left,char[s[right]])
            max_len = max(max_len,right - left + 1)
            char[s[right]] = right + 1
        return max_len

        