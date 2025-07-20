class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        maxCount = 0
        maxlen = 0
        for right in range(len(s)):
            count[s[right]] += 1
            maxCount = max(maxCount,count[s[right]])
            l = right - left + 1
            if l - maxCount > k:
                count[s[left]] -= 1
                left += 1
            maxlen = max(maxlen,right-left+1)
        return maxlen


        