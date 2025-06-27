class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # return len(set(sentence)) == 26
        alph = [0]*26
        for i in sentence:
            alph[ord(i) - ord('a')] += 1
        for i in alph:
            if i==0:
                return False
        return True

        