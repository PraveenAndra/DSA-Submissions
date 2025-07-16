class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        def subtractOne(num):
            i = len(num) - 1
            while i >= 0:
                if num[i] == '0':
                    num[i] = '9'
                    i-=1
                else:
                    num[i] = str(int(num[i])-1)
                    break
            if num[0] == "0":
                num.pop(0)
            return "".join(num) or "0"


        def countUpto(num,ind,tight,s):
            l = len(num)
            cache = {}
            def dp(ind,tight,s):
                if s> max_sum:
                    return 0
                if ind == l:
                    return 1 if min_sum <= s <=max_sum else 0
                if (ind,tight,s) in cache:
                    return cache[(ind,tight,s)]
                limit = int(num[ind]) if tight else 9
                res = 0
                for d in range(limit+1):
                    new = tight and (d == limit)
                    res = (res+ dp(ind+1,new,s+d)) %  (10**9+7)
                cache[(ind,tight,s)] = res
                return res
            return dp(ind,tight,s)
        
        num1m1 = subtractOne(list(num1))
        res1 = countUpto(num2,0,1,0)
        res2 = countUpto(num1m1,0,1,0)
        return (res1-res2) % (10**9+7)
        