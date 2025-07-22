class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = defaultdict(int)
        count = 0
        for i in t:
            counter[i] += 1
        count = len(counter)
        left = 0
        res = float('inf'),None,None
        for right in range(len(s)):
            if s[right] in counter:
                counter[s[right]] -= 1
                if counter[s[right]] == 0:
                    count -= 1
            
            while left <=right and count == 0:
                c = s[left]
                if right-left+1 < res[0]:
                    res = (right-left+1,left,right)
                if c in counter:
                    counter[c]+= 1
                    if counter[c] > 0:
                        count += 1
                left += 1
            # print(right,res,counter)
        return s[res[1]:res[2]+1] if res[0] != float('inf') else ""
            

            
        