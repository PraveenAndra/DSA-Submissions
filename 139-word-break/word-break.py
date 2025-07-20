class TrieNode:
    def __init__(self):
        self.trie = {}
        self.last = False
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode()
        for word in wordDict:
            curr = root
            for char in word:
                if char not in curr.trie:
                    curr.trie[char] = TrieNode()
                curr = curr.trie[char]
            curr.last = True
        l = 0
        dp = [False]*len(s)
        for i in range(len(s)):
            if i==0 or dp[i-1]:
                curr = root
                for j in range(i,len(s)):
                    if s[j] in curr.trie:
                        curr = curr.trie[s[j]]
                    else:
                        break
                    if curr.last:
                        dp[j] = True
        return dp[-1]
                

        