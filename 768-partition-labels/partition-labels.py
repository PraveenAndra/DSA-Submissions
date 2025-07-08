class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_indexes = {}
        for i in range(len(s)-1,-1,-1):
            if s[i] not in last_indexes:
                last_indexes[s[i]] = i
        # print(last_indexes)
        res = []
        left = 0
        right = last_indexes[s[0]]
        for i in range(len(s)-1):
            if i == right:
                res.append(right-left+1)
                left = right+1
                right = last_indexes[s[left]]
            else:
                right = max(right,last_indexes[s[i]])
        res.append(right-left+1)
        return res


            

        