class Solution:
    def firstUniqChar(self, s: str) -> int:
        lookup = defaultdict(int)
        for i in s:
            lookup[i] += 1
        for i in range(len(s)):
            if lookup[s[i]] == 1:
                return i
        return -1
