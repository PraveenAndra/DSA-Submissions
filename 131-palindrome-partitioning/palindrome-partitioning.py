class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def is_palindrome(k):
            return k==k[::-1]

        def backtrack(l,arr):
            if not l:
                res.append(arr[:])
                return
            for i in range(1,len(l)+1):
                if is_palindrome(l[:i]):
                    backtrack(l[i:],arr+[l[:i]])
        backtrack(s,[])
        return res
                

        
        