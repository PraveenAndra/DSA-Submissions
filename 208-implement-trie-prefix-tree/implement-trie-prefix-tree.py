class TrieNode:
    def __init__(self):
        self.trie = {}
        self.last = False

class Trie:

    def __init__(self):
        self.node = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.node
        for ind in range(len(word)):
            i = word[ind]
            if i not in curr.trie:
                curr.trie[i] = TrieNode()
            
            curr = curr.trie[i]
            if ind == len(word)-1:
                curr.last = True
            


    def search(self, word: str) -> bool:
        curr = self.node
        for i in range(len(word)):
            if word[i] not in curr.trie:
                return False
            curr = curr.trie[word[i]]
        return curr.last 

    def startsWith(self, prefix: str) -> bool:
        curr = self.node
        for i in range(len(prefix)):
            if prefix[i] not in curr.trie:
                return False
            curr = curr.trie[prefix[i]]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)