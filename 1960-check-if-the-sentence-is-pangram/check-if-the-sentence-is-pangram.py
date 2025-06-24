class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(list(set(sentence))) == 26
        