class TrieNode:
    def __init__(self):
        self.trie = {}
        self.last = False
class Trie:

    def __init__(self):
        self.trie = TrieNode() 

    def insert(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c not in curr.trie:
                curr.trie[c] = TrieNode()
            curr = curr.trie[c]
        curr.last = True
        
    def search(self, word: str) -> bool:
        curr = self.trie
        for c in word:
            if c not in curr.trie:
                return False
            curr = curr.trie[c]
        return curr.last

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for c in prefix:
            if c not in curr.trie:
                return False
            curr = curr.trie[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)