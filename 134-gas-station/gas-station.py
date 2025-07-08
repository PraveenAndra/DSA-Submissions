class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gain = [x-y for x,y in zip(gas,cost)]
        curr = 0
        res = 0
        for i in range(len(gain)):
            curr += gain[i]
            if curr < 0:
                curr = 0
                res = i + 1
        return res if sum(gain) >= 0 else -1


        