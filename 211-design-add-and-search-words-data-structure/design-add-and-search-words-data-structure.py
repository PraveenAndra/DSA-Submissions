class TrieNode:
    def __init__(self):
        self.trie = {}
        self.last = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.trie:
                curr.trie[c] = TrieNode()
            curr = curr.trie[c]
        curr.last = True
    def find(self,word,root):
        for i,c in enumerate(word):
            # print(c,root.trie)
            if c == ".":
                for k in root.trie:
                    if self.find(word[i+1:],root.trie[k]):
                        return True
            if c not in root.trie:
                return False
            root = root.trie[c]
            
        return root.last
    def search(self, word: str) -> bool:
        return self.find(word,self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)