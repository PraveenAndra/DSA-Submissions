class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        # Convert the list of words into a set for faster lookups
        dictionary = set(words)
        answer = []

        # Iterate over each word in the words list
        for word in words:
            length = len(word)
            # DP array to store whether a substring can be formed by concatenation
            dp = [False] * (length + 1)
            dp[0] = True  # Base case: empty string is always valid

            # For each possible position in the word
            for i in range(1, length + 1):
                for j in range(1 if i == length else 0, i):  # Start j from 1 if i == length (don't consider the whole word)
                    if dp[j] and word[j:i] in dictionary:
                        dp[i] = True
                        break  # No need to continue if we found a valid split

            # If dp[length] is True, the word can be formed by concatenating other words
            if dp[length]:
                answer.append(word)

        return answer