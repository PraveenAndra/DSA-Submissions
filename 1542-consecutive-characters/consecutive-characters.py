class Solution:
    def maxPower(self, s: str) -> int:
        maxPower = 1
        power = 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                power += 1
            else:
                maxPower = max(maxPower,power)
                power = 1
        return max(maxPower,power)